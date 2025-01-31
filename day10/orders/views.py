import requests
from django.shortcuts import get_object_or_404
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer
from products.models import Product

class InitiatePaymentView(APIView):
    """
    Initiates the payment with Khalti for the order.
    """
    def post(self, request):
        # Use the updated OrderSerializer
        serializer = OrderSerializer(data=request.data, context={'request': request})  # Pass request context here
        if serializer.is_valid():
            order = serializer.save()

            # Calculate the total amount from the order items
            try:
                amount = sum(
                    get_object_or_404(Product, id=item['product']).price * item['quantity']
                    for item in request.data['items']
                ) * 100  # Convert to the smallest unit (e.g., cents, paisa)
            except KeyError:
                return Response({"error": "Invalid product data in items"}, status=status.HTTP_400_BAD_REQUEST)

            # Prepare the payment initiation payload
            payload = {
                "return_url": "http://127.0.0.1:8000/api/verify-payment/",
                "website_url": "http://127.0.0.1:8000",
                "amount": int(amount),
                "purchase_order_id": f"Order_{order.id}",
                "purchase_order_name": f"Order {order.id}",
                "customer_info": {
                    "name": request.user.username,
                    "email": request.user.email,
                    "phone": request.data.get("phone", ""),
                },
            }
            headers = {
                'Authorization': f'Key {settings.KHALTI_SECRET_KEY}',
                'Content-Type': 'application/json',
            }

            # Send request to Khalti for payment initiation
            try:
                response = requests.post("https://a.khalti.com/api/v2/epayment/initiate/", headers=headers, json=payload)
                response_data = response.json()

                if response.status_code == 200:
                    order.purchase_order_id = payload["purchase_order_id"]
                    order.save()
                    return Response(response_data, status=status.HTTP_200_OK)
                return Response(response_data, status=response.status_code)

            except requests.RequestException as e:
                return Response({
                    "message": "Failed to initiate payment with Khalti.",
                    "details": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyPaymentView(APIView):
    """
    Verifies a payment with Khalti.
    """
    def get(self, request):
        pidx = request.query_params.get("pidx")
        if not pidx:
            return Response({"message": "Invalid request: Missing pidx."}, status=status.HTTP_400_BAD_REQUEST)

        # Prepare Khalti verification request
        url = "https://a.khalti.com/api/v2/epayment/lookup/"
        headers = {
            'Authorization': f'Key {settings.KHALTI_SECRET_KEY}',
            'Content-Type': 'application/json',
        }
        payload = {"pidx": pidx}

        try:
            # Send POST request to Khalti
            response = requests.post(url, headers=headers, json=payload)
            response_data = response.json()

            if response.status_code == 200 and response_data.get("status") == "Completed":
                purchase_order_id = response_data.get("purchase_order_id")
                order = Order.objects.filter(purchase_order_id=purchase_order_id).first()

                if order:
                    order.payment_status = "Completed"
                    order.save()
                    return Response({
                        "message": "Payment verified successfully.",
                        "data": response_data
                    }, status=status.HTTP_200_OK)

                return Response({
                    "message": "Order not found.",
                    "data": response_data
                }, status=status.HTTP_404_NOT_FOUND)

            return Response({
                "message": "Payment verification failed.",
                "data": response_data
            }, status=response.status_code)

        except requests.RequestException as e:
            return Response({
                "message": "Error communicating with Khalti.",
                "details": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

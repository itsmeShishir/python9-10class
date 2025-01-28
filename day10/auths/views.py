from django.shortcuts import render
from .serializations import UserSerializer, UserRegisterSerializer
from .models import User
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from django.contrib.auth import authenticate, update_session_auth_hash
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import permissions

# Create your views here.
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRegister(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    
# from rest_framework_simplejwt.tokens import RefreshToken
class LoginApi(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = authenticate(email=email, password=password)


        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        if not user:
            return Response({'message': 'Crediancial donenot match'})

        if user is not None:
           update_session_auth_hash(request, user)
           return Response({
            'status': 200,
            'access': access_token,
            'refresh': str(refresh),
            'message': 'Login Success', 
            'username': user.username, 
            "role": user.role,
            "email": user.email
            })
        else:
           return Response({'message': 'Login Failed'})
           
#class Profile section  -> token send in header -> using access token

class Profile(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
    
class changePassword(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserRegisterSerializer

    def get_object(self):
        return self.request.user
    
    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(
                serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=400)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': 200,
                'message': 'Password updated successfully',
            }

            return Response(response)

        return Response(serializer.errors, status=400)


#update profile 
class UpdateProfile(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user   


#class logout 
class logout_user(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        token = request.data.get('token')
        try:
            RefreshToken(token).blacklist()
            return Response({'message': 'Logout Success'})
        except Exception as e:
            return Response({'message': 'Logout Failed'})
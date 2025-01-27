from django.urls import path
from .views import AllCategory, AllProduct, CreateCategory, CreateProduct, DeleteSingleProduct, SingleCategory, SingleProduct, UpdateSingleCategory, DeleteSingleCategory, UpdateSingleProduct
urlpatterns = [
    path('allCategory/', AllCategory.as_view() , name="allcategory" ),
    path('createCategory/', CreateCategory.as_view() , name="createcategory" ),
    path('singlecategory/<int:pk>/', SingleCategory.as_view() , name="singlecategory" ),
    path('updatecategory/<int:pk>/', UpdateSingleCategory.as_view() , name="updatecategory" ),
    path('deletecategory/<int:pk>/', DeleteSingleCategory.as_view() , name="deletecategory" ),
    # product
    path('allProduct/', AllProduct.as_view() , name="allproduct" ),
    path('createProduct/', CreateProduct.as_view() , name="createProduct" ),
    path('singleProduct/<int:pk>/', SingleProduct.as_view() , name="singleProduct" ),
    path('updateProduct/<int:pk>/', UpdateSingleProduct.as_view() , name="updateProduct" ),
    path('deleteProduct/<int:pk>/', DeleteSingleProduct.as_view() , name="deleteProduct" ),
]

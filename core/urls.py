from django.urls import path, include
from .views import *
from rest_framework import routers

# CREAMOS LAS RUTAS DEL API
router = routers.DefaultRouter()
router.register('productos', ProductoViewset)
router.register('tipoproductos', TipoProductoViewset)

urlpatterns = [
    #API
    path('api/', include(router.urls)),
    # RUTAS
    path('', index, name="index"),
    path('indexapi/', indexapi, name="indexapi"),
    path('about/', about, name="about"),
    path('blogsingle/', blogsingle, name="blogsingle"),
    path('blog/', blog, name="blog"),
    path('cart/', cart, name="cart"),
    path('checkout/', checkout, name="checkout"),
    path('contact/', contact, name="contact"),
    path('productsingle/', productsingle, name="productsingle"),
    path('shop/', shop, name="shop"),
    path('wishlist/', wishlist, name="wishlist"),
    #CRUD
    path('add/', add, name="add"),
    path('update/<id>/', update, name="update"),
    path('delete/<id>/', delete, name="delete"),
]
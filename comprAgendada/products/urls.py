from rest_framework import routers
from .views import ProductResource

product_routes = routers.SimpleRouter()
product_routes.register(r'products', ProductResource)

from rest_framework import routers
from .views import HamperResource

hamper_routes = routers.SimpleRouter()
hamper_routes.register(r'hampers', HamperResource)

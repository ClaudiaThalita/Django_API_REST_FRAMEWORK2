from rest_framework import urlpatterns
from app.views import TodoViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.registrer(r'', TodoViewSet)
urlpatterns = router.urls
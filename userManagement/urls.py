from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register("profile", views.ProfileViewset)

urlpatterns = router.urls

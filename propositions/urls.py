from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register("propositions", views.PropViewset)
router.register("downvotes", views.DownvoteViewset)
router.register("upvotes", views.UpvoteViewset)


urlpatterns = router.urls

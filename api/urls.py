from django.urls import path, include
from api import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('user', views.UserViewSet)
account_router = SimpleRouter()
account_router.register('account', views.AccountViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(account_router.urls)),
    path('new_user/', views.CreateUserView.as_view()),
    path("new_account/", views.CreateAccountView.as_view()),
    path("users/<int:pk>/", views.user_detail, name='user_detail'),
]

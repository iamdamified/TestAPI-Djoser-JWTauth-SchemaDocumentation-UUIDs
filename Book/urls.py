from django.urls import path
from .views import ApiHomePage, ApiDetailPage

urlpatterns = [
    path('', ApiHomePage.as_view(), name="home"),
    path('<uuid:id>/', ApiDetailPage.as_view(), name="detail_page")
]
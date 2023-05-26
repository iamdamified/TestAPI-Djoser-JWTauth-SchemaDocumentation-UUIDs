"""
URL configuration for Authentication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', include("Book.urls")),# this endpoint/url handles the normal API/Serialization and redirects url/endpoint to Book App urls paths.
    path('auth/', include('djoser.urls')),# endpoints from here handles path tp Djoser that makes testing API in DRF easier
    path('auth/', include('djoser.urls.jwt')), #Djoser JWT specific Authentication Testing paths
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),# from this path down is for Swagger documantation download
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc",),# Not tried yet
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"), #View and Edit# new
]

# However, please note that POSTMAN is best for Documentation than swagger.
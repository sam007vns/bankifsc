from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns=[
path("",views.home,name="home"),
path("<str:select_bank_>",views.select_bank,name="select_bank_"),
path("<str:select_bank_>/<str:select_state_>",views.select_state,name="select_state_"),
path("<str:select_bank_>/<str:select_state_>/<str:select_city_>",views.select_city,name="select_city_"),
path("<str:select_bank_>/<str:select_state_>/<str:select_city_>/<str:branch_>",views.branch,name="branch_"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
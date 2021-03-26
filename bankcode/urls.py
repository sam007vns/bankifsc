"""newtruth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from main.sitemaps import BankNamesSitemap
admin.site.site_header = 'AnotherView-IFSC Admin'
admin.site.index_title = 'Authors Dashboard'
admin.site.site_title = 'AnotherView IFSC' 

sitemaps={
	'BankNames': BankNamesSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    # path('robots.txt/',include('robots.urls')),
    path('',include('main.urls')),
]

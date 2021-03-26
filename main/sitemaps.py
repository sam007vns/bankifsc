from django.contrib.sitemaps import Sitemap
from .models import BankNames
from django.urls import reverse

class BankNamesSitemap(Sitemap):
	def items(self):
		return BankNames.objects.all()
# class StaticViewSitemap(Sitemap):
# 	def items(self):
# 		return['tech-contact']
# 	def location(self, item):
# 		return reverse(item)

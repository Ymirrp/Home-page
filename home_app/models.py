from django.contrib.auth.models import User
from django.db import models


class TopSites(models.Model):
    CATEGORIES = [
        ('HOBB', 'Áhugamál'),
        ('BOOK', 'Bókamerki'),
        ('NEWS', 'Fréttir'),
        ('SPOR', 'Íþróttir'),
        ('GAME', 'Leikir'),
        ('EDUC', 'Nám'),
        ('SOCI', 'Samfélagsmiðlar'),
        ('SHOP', 'Versla'),
        ('WORK', 'Vinna'),
        ('FAVO', 'Uppáhalds'),
    ]
    id = models.AutoField(primary_key=True)
    _user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.CharField(max_length=4, choices=CATEGORIES, default='FAVO')
    name = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=False)
    clicks = models.IntegerField(default=0)

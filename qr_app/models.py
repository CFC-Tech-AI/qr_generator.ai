from django.db import models

class QRData(models.Model):
    data = models.CharField(max_length=255)

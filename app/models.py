from django.utils import timezone
from django.db import models

class Vehicle(models.Model):
    plate_number = models.CharField(max_length=15)
    driver_name = models.CharField(max_length=100)
    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True, blank=True)
    entry_weight = models.FloatField(null=True, blank=True)
    exit_weight = models.FloatField(null=True, blank=True)
    net_weight = models.FloatField(null=True, blank=True)


    def save(self, *args, **kwargs):
        if self.exit_weight and not self.exit_time:
            self.exit_time = timezone.now()
        if self.exit_weight and self.entry_weight:
            self.net_weight = self.exit_weight - self.entry_weight
        super().save(*args, **kwargs)



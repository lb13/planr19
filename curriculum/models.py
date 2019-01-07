from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Offering(models.Model):
    code = models.CharField(max_length=20, default="to be assigned")
    name = models.CharField(max_length=200)
    web_description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code
    
    def get_absolute_url(self):
        return reverse('offering-detail', kwargs={'pk': self.pk})
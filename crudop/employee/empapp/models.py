from django.db import models
from django.urls import reverse


class Employee(models.Model):
    empname = models.CharField(max_length=100)
    empemail = models.EmailField(unique=True)
    empcontact = models.CharField(max_length=100)

    # def get_absolute_url(self):
    #     return reverse('detail', kwargs={'pk':self.pk,})



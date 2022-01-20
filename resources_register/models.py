from django.db import models

# Create your models here.
class Resource(models.Model):
  name = models.CharField(max_length=100)

  class Meta:
    app_label = "resources_register"

  def __str__(self):
    return self.name
from django.db import models
from django.contrib.auth.models import User
from drawers.models import Drawer
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Item(models.Model):
  name = models.CharField(max_length=255, blank=False)
  units = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  drawer = models.ForeignKey(Drawer, on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.name

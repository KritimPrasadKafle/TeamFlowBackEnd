from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, max_length = 50)
    phone_number = models.CharField(unique=True, max_length= 15)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 50)
    avatar = models.CharField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField()
    updated_at = models.DateField()



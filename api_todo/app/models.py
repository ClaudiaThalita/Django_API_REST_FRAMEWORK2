from django.db import models

# Create your models here.
# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Todo(BaseModel):
    name = models.CharField(max_length=120)
    done = models.BooleanField(default=False)
    
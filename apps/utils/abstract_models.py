from django.db import models
import uuid

class CommonFields(models.Model):
    """Common fields for all models."""
    id = models.UUIDField(unique=True, default=uuid.uuid4, primary_key=True, editable=False, db_index=True)
    
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
    objects = models.Manager()
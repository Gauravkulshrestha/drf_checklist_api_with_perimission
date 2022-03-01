from django.db import models
from django.contrib.auth.models import User

class Checklist(models.Model):
    title = models.CharField(max_length=120)
    is_deleted = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)    
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class ChecklistItem(models.Model):
    text = models.CharField(max_length=120)
    is_checked = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE, related_name="checklist")    
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
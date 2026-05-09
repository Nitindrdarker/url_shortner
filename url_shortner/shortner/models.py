from django.db import models

class URL(models.Model):
    original_url = models.URLField(unique=True)
    short_code = models.CharField(max_length=10, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.short_code
    
 

class ClickEvent(models.Model):
    url = models.ForeignKey(URL, on_delete=models.CASCADE)
    clicked_at = models.DateTimeField(auto_now_add=True, db_index=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    request_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.request_id
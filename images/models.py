from django.db import models


class Image(models.Model):
    label=models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    size=models.DecimalField(max_digits=10, decimal_places=2)
    user=models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='images')
    upload_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-upload_at']
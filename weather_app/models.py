from django.db import models

class SearchHistory(models.Model):
    city = models.CharField(max_length=100)
    count = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} - {self.count} раз(а)"

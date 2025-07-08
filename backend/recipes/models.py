from django.db import models
class Recipe(models.Model):
    cuisine = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    rating = models.FloatField(null=True)
    prep_time = models.IntegerField(null=True)
    cook_time = models.IntegerField(null=True)
    total_time = models.IntegerField(null=True)
    description = models.TextField()
    nutrients = models.JSONField(null=True)  # JSON
    serves = models.CharField(max_length=100)
    def __str__(self):
        return self.title

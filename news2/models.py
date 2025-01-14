from django.db import models

class AddNews(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='news_images/')
    

    def __str__(self):
        return self.title





    
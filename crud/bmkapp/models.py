from django.db import models

# 북마크 기능

class Bookmark(models.Model):
    site_name = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return self.site_name + " - " + self.url
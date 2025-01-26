from django.db import models


class Classroom(models.Model):
    title = models.CharField(max_length=255)
    short_introduction = models.CharField(max_length=500)
    course_description = models.TextField()
    course_image = models.ImageField(upload_to='course_images/')
    preview_video_link = models.URLField(max_length=200)
    tags = models.CharField(max_length=255)
    categories = models.CharField(max_length=255)
    published = models.BooleanField(default=False)
    upcoming = models.BooleanField(default=False)
    published_on = models.DateTimeField(null=True, blank=True)
    paid_course = models.BooleanField(default=False)
    course_price = models.DecimalField(max_digits=10, decimal_places=2)

    slug = models.SlugField(max_length=255, unique=True)
    total_rating = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    number_of_ratings = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def average_rating(self):
        if self.number_of_ratings == 0:
            return 0
        return self.total_rating / self.number_of_ratings

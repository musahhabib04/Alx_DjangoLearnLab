from django.db import models

class Shelf(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class ShelfBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title

# Create your models here.

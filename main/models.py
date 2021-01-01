from django.db import models

# Create your models here.
class Book(models.Model):
    tittle = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Author(models.Model):
    first_name= models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes= models.TextField()
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    book_written = models.ManyToManyField(
        Book,
        related_name="written_by"
    )


from django.db import models

# Create your models here.

class BookModel(models.Model):

   bookname = models.CharField(max_length = 50)
   subject = models.CharField(max_length = 50)
   price = models.IntegerField()


   class Meta:
      db_table = "books"

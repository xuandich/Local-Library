from django.db import models

# Create your models here.


class Author(models.Model):
    """ Model Tác Giả
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)


class Book(models.Model):
    """ Model Tác Phẩm
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    publish_date = models.DateField()
    authors = models.ManyToManyField("Author")
    summary = models.CharField(max_length=500, blank=True)
    categorys = models.ManyToManyField("Category")

class Category(models.Model):
    """ Model Thể Loại
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
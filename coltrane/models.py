from django.db import models
import datetime

# Create your models here.

class Category(models.Model):
  title = models.CharField(max_length=250)
  slug = models.SlugField(unique=True)
  description = models.TextField()

  class Meta:
    verbose_name_plural = "Categories"

  class Admin:
    pass

  def __unicode__(self):
    return self.title

class Entry(models.Model):
  title = models.CharField(max_length=250)
  excerpt = models.TextField(blank=True)
  body = models.TextField()
  pub_date = models.DateTimeField(default=datetime.datetime.now)
  slug = models.SligField(prepopulate_from=['title'],
                          unique_for_date='pub_date')

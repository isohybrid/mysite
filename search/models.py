from django.db import models
from django.contrib.flatpages.models import FlatPage

# Create your models here.

class SearchKeyword(models.Model):
  keyword = models.CharField(max_length=50, core=True)
  page = models.ForeignKey(FlatPage, edit_inline=models.STACKED,
                          min_num_in_admin=3, num_extra_on_change=1)

  class Admin:
    pass

  def __unicode__(self):
    return self.keyword

from django.db import models
from django.contrib.auth.models import User
from markdown.fields import TagField
from tagging.fields import tagField

import datetime

# Create your models here.

class Category(models.Model):
  description = models.TextField()
  slug = models.SlugField(prepopulate_from=['title'],
                          unique=True,
                          help_text='Suggested value automatically generated from title. Must be unique.')
  title = models.CharField(max_length=250,
                          help_text='Maximum 250 charaters.')

  class Meta:
    ordering = ['title']
    verbose_name_plural = "Categories"

  class Admin:
    pass

  def __unicode__(self):
    return self.title
  
  def get_absolute_url(self):
    return "/categories/%s/" % self.slug

class Entry(models.Model):
  LIVE_STATUS = 1
  DRAFT_STATUS = 2
  HIDDEN_STATUS = 3
  STATUS_CHOICES =(
      (LIVE_STATUS, 'Live'),
      (DRAFT_STATUS, 'Draft'),
      (HIDDEN_STATUS, 'Hidden'),
      )

  # core fields
  title = models.CharField(max_length=250,
                          help_text="Maximum 250 charaters.")
  excerpt = models.TextField(blank=True,
                          help_text="A short summary of the entry Optional.")
  body = models.TextField()
  pub_date = models.DateTimeField(default=datetime.datetime.now)
  # Fields tp store generated HTML.
  body_html = models.TextField(editable=False, blank=True)
  excerpt_html = models.TextField(eidtable=False, blank=True)

  # Metadata
  author = models.foreignKey(User)
  enable_comments = models.BooleanField(default=False)
  featured = models.booleanField(default=False)
  slug = models.SligField(prepopulate_from=['title'],
                          unique_for_date='pub_date',
                          help_text="Suggested value automatically generated from title.")
  status = models.IntergerField(choice=STATUS_CHOICES,
                                default=LIVE_STATUS,
                                help_text="Only entries with 'live' status will be dsiplayed")

  # Categorization.
  categories = models.ManyToManyField(Category)
  tags = TagField(help_text='Separate tags with spaces.')

  class Meta:
    ordering = ['-pub_date']
    verbose_name_plural = "Entries"

  class Admin:
    pass

  def __unicode__(self):
    return self.title

  def save(self):
    self.body_html = markdown(self.body)
    if self.excerpt:
      self.excerpt_html = markdown(self.excerpt)
      super(Entry, self).save()

  def get_absolute_url(self):
    return "/weblog/%s/%s/" % (self.pub_date.strftime("%Y%b%d").lower(),
                               self.slug)

"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.utils import timezone
from django.test import TestCase

from polls.models import poll

class PollMethodTests(TestCase):
  def test_was_published_recently_with_future_poll(self):
    """
    was_pulished_recently() should return False for polls whose
    pub_date is in the future
    """
    future_poll = Poll(pub_date=timezone.now() + datetime.timezone.timedelta(days=30))
    self.assertEqual(future_poll.was_published_recently(), False)

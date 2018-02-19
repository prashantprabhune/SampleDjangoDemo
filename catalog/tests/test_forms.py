from django.test import TestCase

# Create your tests here.

import datetime
from django.utils import timezone
from catalog.forms import RenewBookForm

class RenewBookFormTest(TestCase):
             
    def test_renew_form_date_field_help_text(self):
        """
        Test renewal_date help_text is as expected.
        """
        form = RenewBookForm()
self.assertEqual(form.fields['renewal_date'].help_text,'Enter a date between now and 4 weeks (default 3).')

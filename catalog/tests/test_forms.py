from django.test import TestCase

# Create your tests here.

import datetime
from django.utils import timezone
from catalog.forms import RenewBookForm

class RenewBookFormTest(TestCase):

    def test_renew_form_date_in_past(self):
        """
        Test form is invalid if renewal_date is before today
        """
        date = datetime.date.today() - datetime.timedelta(days=1)
        form_data = {'renewal_date': date}
        form = RenewBookForm(data=form_data)
        self.assertFalse(form.is_valid())

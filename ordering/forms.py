from . import models
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = models.Booking
        fields = ["user","started_at", "ended_at"]

from django.db import models
from django import forms

# Create your models here.
class Wish(models.Model):
	email = models.CharField(max_length=200)
	wish = models.CharField(max_length=200)
	status = models.CharField(max_length=200)
	jira_ticket = models.CharField(max_length=200)
	date = models.DateTimeField('date published')

class WishForm(forms.Form):
    email = forms.EmailField(max_length=100)
    wish = forms.CharField()
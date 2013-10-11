from django.db import models
class JiraPlugin(models.Model):
	login = models.CharField(max_length=200)
	password = models.CharField(max_length=200)

class JiraTicket(models.Model):
	project_code = models.CharField(max_length=20)
	summary = models.CharField(max_length=256)
	description = models.CharField(max_length=1024)
	component = models.CharField(max_length=64)
	issue_type = models.CharField(max_length=32)
	
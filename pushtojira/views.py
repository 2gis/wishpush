# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from dashboard.models import JiraTicket, JiraPlugin, Wish
import django.utils.simplejson as json
import httplib
import base64

def create_issue(request):
	return None

def edit_issue(request):
	return None

def list_issues(request):

	return None

def list_links():
	jiraplugin = JiraPlugin(login='login', password='qweqweqwe')
	cred = jiraplugin.get_headers()
	conn = httplib.HTTPConnection(jiraplugin.jira_instance)


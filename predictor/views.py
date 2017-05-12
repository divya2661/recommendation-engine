# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, JsonResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def dummy_json(request):
    return JsonResponse({"lat":12.20,"lot":12.23})
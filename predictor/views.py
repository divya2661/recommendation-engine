# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, JsonResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def dummy_json(request):
    return JsonResponse({"locations":[
                                {"lat": 12.9354381, "lon": 77.5617222},
                                {"lat": 12.9560138, "lon": 77.5916371},
                                {"lat": 12.9560126, "lon": 77.5915512},
                                {"lat": 12.9317898, "lon": 77.629813},
                                {"lat": 12.9422533, "lon": 77.6203564}]})



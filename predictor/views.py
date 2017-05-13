# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, JsonResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def dummy_json(request):
    return JsonResponse({
  "items": [
    {
      "name": "Koramangla 4th block",
      "lat": 12.9354381,
      "lon": 77.5617222
    },
    {
      "name": "Koramangla 5th block",
      "lat": 12.9560138,
      "lon": 77.5916371
    },
    {
      "name": "Koramangla 6th block",
      "lat": 12.9560126,
      "lon": 77.5915512
    },
    {
      "name": "Koramangla 7th block",
      "lat": 12.9317898,
      "lon": 77.629813
    },
    {
      "name": "Koramangla 8th block",
      "lat": 12.9422533,
      "lon": 77.6203564
    }
  ]
})

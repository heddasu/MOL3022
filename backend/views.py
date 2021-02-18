from django.shortcuts import render
from backend.models import Matrix
import requests
from rest_framework import viewsets
from django.core import serializers
from rest_framework.utils import json
from django.http import HttpResponse, JsonResponse






def get_matrix(request):
    all_matrices = {}

    url = "http://jaspar.genereg.net/api/v1/species/9606/?page_size=1300"
    response = requests.get(url)
    data = response.json()
    matrix = data["results"]
    
    all_matrices = post_matrix(matrix)

    qs_json = serializers.serialize('json', all_matrices)

    return HttpResponse(qs_json, content_type='application/json')

    
def post_matrix(matrix):
    all_matrix = {}

    for i in matrix:
        matrix_data = Matrix(
            matrix_id = i["matrix_id"]
        )
        matrix_data.save()
    
    all_matrix = Matrix.objects.all()

    return all_matrix



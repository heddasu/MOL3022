from django.shortcuts import render
from backend.models import Matrix
import requests
from rest_framework import viewsets
from django.core import serializers
from rest_framework.utils import json
from django.http import HttpResponse, JsonResponse


def get_matrix(request):
    all_matrices = {}

    url = "http://jaspar.genereg.net/api/v1/species/9606/?page=1&page_size=1000"
    response = requests.get(url)
    data = response.json()
    matrix = data["results"]
    
    post_matrix(matrix)

    url = "http://jaspar.genereg.net/api/v1/species/9606/?page=2&page_size=1000"
    response = requests.get(url)
    data = response.json()
    matrix = data["results"]

    post_matrix(matrix)

    qs_json = serializers.serialize('json', all_matrices)

    return HttpResponse(qs_json, content_type='application/json')

    
def post_matrix(matrix):

    for i in matrix:
        matrix_data = Matrix(
            matrix_id = i["matrix_id"],
            name = i["name"]
        )
        matrix_data.save()


def matrix_detail(request, matrix_id):
    matrix = Matrix.objects.get(matrix_id=matrix_id)
    #qs_json = serializers.serialize('json', matrix)

    return HttpResponse(matrix, content_type='application/json')


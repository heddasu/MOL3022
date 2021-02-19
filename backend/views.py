from django.shortcuts import render
from backend.models import Matrix, Pfm
import requests
from rest_framework import viewsets
from django.core import serializers
from rest_framework.utils import json
from django.http import HttpResponse, JsonResponse


def get_matrix(request):
    all_matrices = {}

    url_matrix = "http://jaspar.genereg.net/api/v1/species/9606/?page=1&page_size=1000"
    response_matrix = requests.get(url_matrix)
    data = response_matrix.json()
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
    url_pfm = "http://jaspar.genereg.net/api/v1/matrix/"

    for i in matrix:

        m_id = i["matrix_id"]

        response_pfm = requests.get(url_pfm + m_id + "/?format=json")
        data = response_pfm.json()
        atcg = data["pfm"]
        print("DETTE ER A", atcg["A"])

        pfm_data = Pfm(
            adenin = atcg["A"],
            thymine = atcg["T"],
            cytosine = atcg["C"],
            guanine = atcg["G"],
        )
        pfm_data.save()

        matrix_data = Matrix(
            matrix_id = m_id,
            name = i["name"],
            pfm = pfm_data
        )
        matrix_data.save()



def matrix_detail(request, matrix_id):
    matrix = Matrix.objects.get(matrix_id=matrix_id)
    #qs_json = serializers.serialize('json', matrix)

    return HttpResponse(matrix, content_type='application/json')


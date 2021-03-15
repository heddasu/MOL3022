from rest_framework import serializers
from backend.models import Pfm, Matrix

class PfmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pfm
        fields = ["adenin", "thymine", "cytosine", "guanine"]

class MatrixSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matrix
        fields = ["matrix_id", "name", "pfm"]
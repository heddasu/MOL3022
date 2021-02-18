from rest_framework import serializers
from models import Pfm, Matrix

# class PfmSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Pfm
#         fields = ["adenin", "thymine", "cytosine", "guanin"]

class MatrixSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matrix
        fields = ["matrix_id", "name", "pfm"]
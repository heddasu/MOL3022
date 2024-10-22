from backend.models import Matrix, Pfm
from rest_framework import viewsets, status
from backend.serializers import MatrixSerializer, PfmSerializer
from backend.calculations import tranform_pfm_object_to_matrix, calculate_number_of_sites, calculate_pwm, transform_pfm_to_pwm, compute_sequence_prob
import json
from rest_framework.response import Response


class MatrixViewSet(viewsets.ModelViewSet):
    queryset = Matrix.objects.all()
    serializer_class = MatrixSerializer

    def get_queryset(self):
        queryset = self.queryset
        
        matrix_id = self.request.query_params.get("id", None)

        if matrix_id is not None:
            try:
                queryset = Matrix.objects.filter(matrix_id=matrix_id)
            except ValueError:
                print("Not valid matrix ID.")

        return queryset.order_by('matrix_id')#.values('matrix_id').order_by('matrix_id')




    def create(self, request, *args, **kwargs):

        queryset = self.queryset

        if not (self.request.data.get("dnaSequence") and self.request.data.get("motifsChosen")):
            return Response(
                {"message": "You must have both a DNA sequence and chosen motif(s)."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        data = json.loads(json.dumps(self.request.data))

        dna_sequence = data.get("dnaSequence")
        relevant_matrices = queryset.filter(matrix_id__in=(data.get("motifsChosen")))
        
        results = []

        for matrix in relevant_matrices:
            pfm_result = Pfm.objects.filter(id=matrix.pfm.id)
            for pfm in pfm_result:
                data = {}
                pfm_matrix = tranform_pfm_object_to_matrix(pfm)
                calc_pwm = transform_pfm_to_pwm(pfm_matrix)
                probability = compute_sequence_prob(calc_pwm, dna_sequence)
                data["id"] = matrix.matrix_id 
                data["probability"] = probability
                results.append(data)

        return Response(
            results,
            status=status.HTTP_200_OK,
        )



class PfmViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pfm.objects.all()
    serializer_class = PfmSerializer

    def get_queryset(self):
        queryset = self.queryset
            
        pfm_id = self.request.query_params.get("id", None)

        if pfm_id is not None:
            try:
                queryset = Pfm.objects.filter(id=pfm_id)
            except ValueError:
                print("Not valid PFM ID.")

        return queryset



"""
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


"""
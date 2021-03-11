from backend.models import Matrix, Pfm
from rest_framework import viewsets
from backend.serializers import MatrixSerializer, PfmSerializer
# from backend.calculations import 
from backend.calculations import tranform_pfm_object_to_matrix, calculate_number_of_sites, calculate_pwm, transform_pfm_to_pwm, compute_sequence_prob




class MatrixViewSet(viewsets.ModelViewSet):
    queryset = Matrix.objects.all()
    serializer_class = MatrixSerializer

    def get_queryset(self):

        """pfm = Pfm.objects.filter(id=3)
        for p in pfm:
            pfm_matrix = tranform_pfm_object_to_matrix(p)
        print('PFM-matrix', pfm_matrix)
        count_sites = calculate_number_of_sites(pfm_matrix)  
        calc_pwm = transform_pfm_to_pwm(pfm_matrix)
        print('PWM_matrix', calc_pwm)

        print('Calculate sequences', compute_sequence_prob(calc_pwm, 'AAAAAAAAAAAA'))"""


        queryset = self.queryset
        
        matrix_id = self.request.query_params.get("id", None)

        if matrix_id is not None:
            try:
                queryset = Matrix.objects.filter(matrix_id=matrix_id)
            except ValueError:
                print("Not valid matrix ID")

        return queryset.values('matrix_id')

class PfmViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pfm.objects.all()
    serializer_class = PfmSerializer

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



def matrix_detail(request, matrix_id):
    matrix = Matrix.objects.get(matrix_id=matrix_id)
    #qs_json = serializers.serialize('json', matrix)

    return HttpResponse(matrix, content_type='application/json')

"""
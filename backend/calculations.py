import math
import numpy
from backend.models import Pfm




base_index = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3
}

def tranform_pfm_object_to_matrix(pfm):
    pfm_matrix = []
    pfm_matrix.append(pfm.adenin)
    pfm_matrix.append(pfm.thymine)
    pfm_matrix.append(pfm.cytosine)
    pfm_matrix.append(pfm.guanine)
    return pfm_matrix


def calculate_number_of_sites(pfm):
    pfm = numpy.array(pfm)
    count = numpy.sum(pfm, axis=0)
    return count[0]


# Compute pwm value for a base
# Pseudocount is calculated by taking the square root of the number of sites.
# Background frequency is set to 0.25 assuming it is uniform.
def calculate_pwm(freq, sites_count, bg=0.25):
    p = (freq + (math.sqrt(sites_count) * 1/4)) / (sites_count + (4 * (math.sqrt(sites_count) * 1/4)))
    pwm = math.log(p/bg,2)
    return pwm


def transform_pfm_to_pwm(pfm_matrix):
    pwm_matrix = []
    sites_count = calculate_number_of_sites(pfm_matrix)
    for i in range(4):
        base_list= []
        for j in range(len(pfm_matrix[0])):
            value = calculate_pwm(pfm_matrix[i][j], sites_count, bg=0.25)
            base_list.append(value)
        pwm_matrix.append(base_list)
    return pwm_matrix


#compute probability for the motif at all given positions in the sequence
def compute_sequence_prob(pwm, sequence):
    motif_length = len(pwm[0])
    prob = [0]*(len(sequence) - motif_length+1) 
    for i in range(len(sequence) - motif_length+1):
        prob_score = []

        for j in range(i, i + motif_length):
            index_of_base = base_index[sequence[j]]
            prob_score.append(pwm[index_of_base][j - i])
        prob[i]=sum(prob_score)

    return prob #TODO: ta vare  på index til proben 


def main():
    print("Hello World!")

if __name__ == "__main__":
    main()
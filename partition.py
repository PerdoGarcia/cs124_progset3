import sys
import random
import math


max_iter = 25000

def residual(s, arr):
    return abs(sum([s[i]*arr[i] for i in range(len(arr))]))



# Karmarkar-Karp algorithm
def karmarkar_karp(arr):
    while len(arr) > 1:
        arr.sort()
        arr[-1] = arr[-1] - arr[-2]
        arr.pop(-2)
    return arr[0]



def repeated_random(arr):
    s = [s.append(random.choice([1, -1])) for _ in range(len(arr))]
    
    for _ in range(max_iter):
        s_new = [random.choice([1, -1]) for _ in range(len(arr))]
        if residual(s_new, arr) < residual(s,arr):
            s = s_new
            if s == 0:
                return s
    return s
    

def hill_climbing(arr):
    s = [s.append(random.choice([1, -1])) for _ in range(len(arr))]
    
    for _ in range(max_iter):
        # define neighbors
        n = random.choice(range(len(arr)))
        s_new = s
        s_new[n] = -s_new[n]
        if residual(s_new, arr) < residual(s,arr):
            s = s_new
            if s == 0:
                return s
    return s

def simulated_annealing(arr):
    s = [s.append(random.choice([1, -1])) for _ in range(len(arr))]
    
    s_2p = s
    
    for i in max_iter:
        n = random.choice(range(len(arr)))
        s_1p = s
        
        if residual(s_1p, arr) < residual(s, arr):
            if s_1p == 0:
                return s_1p
            s = s_1p
        else:
            temp = 10 ** 10 * (.8) ** (math.floor(i / 300))
            prob = math.exp((residual(s, arr) - residual(s_1p, arr)) / temp)
            if random.random() < prob:
                s_2p = s
        if residual(s, arr) < residual(s_2p, arr):
            s_2p = s
            if s == 0:
                return s
    return s


def prepart_rr(arr):
    pass

def prepart_hc(arr):
    pass

def prepart_sa(arr):
    pass


def main():
    # Read input
    flag = sys.argv[1]
    algorithm = sys.argv[2]
    input_file = open(sys.argv[3], "r")
    
    array = []
    for line in (input_file):
        array.append(int(line))
        
    
    if algorithm == 0:
        print(karmarkar_karp(array))
    if algorithm == 1:
        print(repeated_random(array))
    if algorithm == 2:
        print(hill_climbing(array))
    if algorithm == 3:
        print(simulated_annealing(array))
    if algorithm == 11:
        print(prepart_rr(array))
    if algorithm == 12:
        print(prepart_hc(array))
    if algorithm == 13:
        print(prepart_sa(array))
    
    
    


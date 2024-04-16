import sys
import random
import math


max_iter = 25000
preprocess = False

def residual(s, arr):
    residue = abs(sum([s[i]*arr[i] for i in range(len(arr))]))
    return residue

# Karmarkar-Karp algorithm
def karmarkar_karp(arr):
    # pq needed
    
    pq = []
    while len(arr) > 1:
        arr.sort()
        arr[-1] = arr[-1] - arr[-2]
        arr.pop(-2)
    return arr[0]

def repeated_random(arr):
    s = [random.choice([1, -1]) for _ in range(len(arr))]
    s_residue = residual(s, arr)
    for _ in range(max_iter):
        s_new = [random.choice([1, -1]) for _ in range(len(arr))]
        s_new_residue = residual(s_new, arr)
        if s_new_residue < s_residue:
            s_residue = s_new_residue
    return s_residue
    

def hill_climbing(arr):
    s = [random.choice([1, -1]) for _ in range(len(arr))]
    s_residue = residual(s, arr)
    for _ in range(max_iter):
        # define neighbors
        n_1 = random.choice(range(len(arr)))
        s_new = s
        s_new[n_1] = -s_new[n_1]
        s_new_residue = residual(s_new, arr)
        
        if s_new_residue < s_residue:
            s_residue = s_new_residue
    return s_residue

def simulated_annealing(arr):
    s = [random.choice([1, -1]) for _ in range(len(arr))]
    s_2p = s
    s_residue = residual(s, arr)
    
    for i in range(max_iter):
        # get neighbors
        n_1 = random.choice(range(len(arr)))
        s_1p = s
        s_1p[n_1] = -s_1p[n_1]
        s_1p_residue = residual(s_1p, arr)
        
        if s_1p_residue < s_residue:
            s_residue = s_1p_residue
            
        else:
            # flip coin with prob T(iter)
            temp = 10 ** 10 * (.8) ** (math.floor(i / 300))
            prob = math.exp((s_residue - s_1p_residue) / temp)
            if random.random() < prob:
                s_residue = s_1p_residue
        # 2p
        s_2p_residue = residual(s_2p, arr)
        if s_residue < s_2p_residue:
            s_2p_residue = s_residue

    return s_2p_residue
    
def prepartition(arr):
    n = len(arr)
    P = [random.randint(0,n-1) for _ in range(n)]
    A_prime = [0] * n

    for i in range(n):
        A_prime[P[i]] += arr[i]     
    return A_prime, P

def nb_partition(part_s, p):
    new_p = p.copy()
    i = random.choice(range(len(p)))
    j = random.choice(range(len(p)))
    
    while i == j:
        j = random.choice(range(len(p)))
    new_p[i] = j
    size = len(part_s)
    A_prime = [0] * size
    for i in range(size):
        A_prime[new_p[i]] += part_s[i]
    
    return A_prime, new_p
    
def pp_rr(arr):
    part_s, _ = prepartition(arr)
    
    for _ in range(max_iter):   
        part_s_new, _ = prepartition(arr)
        if karmarkar_karp(part_s_new) < karmarkar_karp(part_s):
            part_s = part_s_new
    return karmarkar_karp(part_s)

def pp_hc(arr):
    # s is going to be partitioned solution, with the following structure P
    s, P = prepartition(arr)
    
    for _ in range(max_iter):
        # partition arr not s, because is our candidate s, 
        # but arr needs to be saved for the changes in P, we can't go from P -> P' directly
        new_s, new_p = nb_partition(arr, P)
        if karmarkar_karp(new_s) < karmarkar_karp(s):
            s = new_s
            P = new_p
        
    return karmarkar_karp(s)

def pp_sa(arr):
    s, P = prepartition(arr)
    s_2p, s_2p = s, P
    
    for i in range(max_iter):
        new_s, new_p = nb_partition(arr, P)
        kk_new_s = karmarkar_karp(new_s)
        kk_s = karmarkar_karp(s)
        if kk_new_s < kk_s:
            s = new_s
            P = new_p
        else:
            temp = 10 ** 10 * (.8) ** (math.floor(i / 300))
            prob = math.exp((kk_s - kk_new_s) / temp)
            if random.random() < prob:
                s = new_s
                P = new_p
        kk_opt = karmarkar_karp(s_2p)
        if kk_s < kk_opt:
            s_2p = s
            s_2p = P
    return kk_opt

def main():
    # Read input
    flag = sys.argv[1]
    algorithm = int(sys.argv[2])
    input_file = open(sys.argv[3], "r")
    
    array = []
    for line in (input_file):
        array.append(int(line))
   
    # Call the appropriate algorithm
    if algorithm == 0:
        print(karmarkar_karp(array))
    if algorithm == 1:
        print(repeated_random(array))
    if algorithm == 2:
        print(hill_climbing(array))
    if algorithm == 3:
        print(simulated_annealing(array))
    if algorithm == 11:
        print(pp_rr(array))
    if algorithm == 12:
        print(pp_hc(array))
    if algorithm == 13:
        print(pp_sa(array))
    return

main()
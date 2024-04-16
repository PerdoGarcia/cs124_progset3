import sys
import random
import math


max_iter = 25000

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

def prepartition(arr):
    new_arr = [0] * len(arr)
    
    for j in range(1,len(arr)+1):
        d = 1
        for i in range(len(arr)):
            if new_arr[i] == 0:
                new_arr[i] = d
                d = -d
    return new_arr


def repeated_random(arr):
    if sum(arr) % 2 != 0:
        odd = True
    s = [random.choice([1, -1]) for _ in range(len(arr))]
    s_residue = residual(s, arr)
    for _ in range(max_iter):
        s_new = [random.choice([1, -1]) for _ in range(len(arr))]
        s_new_residue = residual(s_new, arr)
        if s_new_residue < s_residue:
            s_residue = s_new_residue
            if s_residue == 0:
                return s_residue
    return s_residue
    

def hill_climbing(arr):
    s = [random.choice([1, -1]) for _ in range(len(arr))]
    s_residue = residual(s, arr)
    for _ in range(max_iter):
        # define neighbors
        n_1 = random.choice(range(len(arr)))
        n_2 = random.choice(range(len(arr)))
        while n_1 != n_2:
            n_2 = random.choice(range(len(arr)))
        s_new = s
        s_new[n_1] = -s_new[n_1]
        s_new[n_2] = -s_new[n_2]
        
        s_new_residue = residual(s_new, arr)
        
        if s_new_residue < s_residue:
            s_residue = s_new_residue
            if s_residue == 0:
                return s_residue
    return s_residue

def simulated_annealing(arr):
    s = [random.choice([1, -1]) for _ in range(len(arr))]
    s_2p = s
    s_residue = residual(s, arr)
    
    for i in max_iter:
        n_1 = random.choice(range(len(arr)))
        n_2 = random.choice(range(len(arr)))
        
        while n_1 != n_2:
            n_2 = random.choice(range(len(arr)))
            
        s_1p = s
        s_1p[n_1] = -s_1p[n_1]
        s_1p[n_2] = -s_1p[n_2]
        s_1p_residue = residual(s_1p, arr)
        
        if s_1p_residue < s_residue:
            if s_1p_residue == 0:
                return s_1p_residue
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
            if s_2p == 0:
                return s_2p

    return s_2p_residue
    

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
        new_array = prepartition(array)
        print(repeated_random(new_array))
    if algorithm == 12:
        new_array = prepartition(array)
        print(hill_climbing(new_array))
    if algorithm == 13:
        new_array = prepartition(array)
        print(simulated_annealing(new_array))
    return

main()
import numpy as np
import math

def csa(sigma, ps, chiN, cs, damps):
    return sigma * math.exp((np.linalg.norm(ps)/chiN - 1) * cs / damps) 

def ppmf(sigma, meanOld_fitness, arfitness, d_param, p_target):
    p_succ = sum(arfitness < meanOld_fitness) / arfitness.size
    return sigma * math.exp(d_param * (p_succ - p_target) / (1 - p_target))



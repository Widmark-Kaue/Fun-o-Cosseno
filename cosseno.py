# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 20:26:25 2019

@author: Widmark Kauê
"""
import numpy as np
from math import factorial

def cosseno (x,N=10):
    assert type(N) == int , "O número de termos não é um int."
    if (abs(x)>np.pi): 
        y=x//np.pi
        while(abs(x)>np.pi):
            if(y%2==0):
                x=x-y*np.pi
            else:
                x=x-(y-1)*np.pi
    z=0
    for n in range(0,N+1):
        z=z+(((-1)**n)*(x**(2*n))/factorial(2*n))
    return z
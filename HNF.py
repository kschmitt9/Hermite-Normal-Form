import numpy as np
import numpy.linalg as lin

def HNF_row(A):
    n = A[0].size-1
    k = n
    
    def red(b):
        for j in range(k):
            q = np.floor(A[j][k]/b)
            if q < 0:
                q += 1
            if q != 0:
                A[j] = A[j]-q*A[k]
            
    def final_red(b):
        for j in range(k,n):
            q = np.floor(A[j+1][k]/b)
            if q < 0:
                q += 1
            if q != 0:
                A[j+1] = A[j+1]-q*A[k]
    
    def col_fin(k):
        u = np.array([A[j][k] for j in range(k+1)])
        i = np.where(u==np.min(u[np.nonzero(u)]))
        
        O = np.array([A[j][k] for j in range(k)])
            
        while lin.norm(O) != 0:
            l = i[0][0]
            
            if l < k:
                A[[k,l]] = A[[l,k]]
            if A[k][k] < 0:
                A[k] = -A[k]
            red(A[k][k])
            
            u = np.array([A[j][k] for j in range(k+1)])
            i = np.where(u==np.min(u[np.nonzero(u)]))

            O = np.array([A[j][k] for j in range(k)])
        
        if A[k][k] < 0:
                A[k] = -A[k]
                
        final_red(A[k][k])
    
    while k > 0:
        col_fin(k)
        k += -1
    
    if A[k][k] < 0:
        A[k] = -A[k]
    
    final_red(A[k][k])
    
    return A
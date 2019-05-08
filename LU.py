def pivot(a,o,s,n,k):
    p = k
    big = abs(a[o[k]][k]/s[o[k]])
    for i in range(k+1,n):
        dummy = abs(a[o[i]][k]/s[o[i]])
        if dummy > big:
            big = dummy
            p = i
    dummy = o[p]
    o[p] = o[k]
    o[k] = dummy

def substitute(a,o,n,b,x):
    for i in range(1,n):
        sum = b[o[i]]
        for j in range(0,i):
            sum = sum - (a[o[i]][j] * b[o[j]])
        b[o[i]] = sum
    x[n-1] = b[o[n-1]]/a[o[n-1]][n-1]
    for i in range(n-2,-1,-1):
        sum = 0
        for j in range(i+1,n):
            sum = sum + (a[o[i]][j] * x[j])
        x[i] = (b[o[i]]-sum)/a[o[i]][i]

def decompose(a,n,tol,o,s):
    for i in range(0,n):
        o[i] = i
        s[i] = abs(a[i][0])
        for j in range(1,n):
            if(abs(a[i][j])>s[i]):
                s[i] = abs(a[i][j])
    for k in range(0,n-1):
        pivot(a,o,s,n,k)
        if(abs(a[o[k]][k]/s[o[k]])<tol):
            return -1
        for i in range(k+1,n):
            factor = a[o[i]][k]/a[o[k]][k]
            a[o[i]][k] = factor
            for j in range(k+1,n):
                a[o[i]][j] = a[o[i]][j] - (factor * a[o[k]][j])
    if(abs(a[o[k]][k]/s[o[k]])<tol):
        return -1
    return 0


def LU(M, b, tol = 1):
    #Tamanio
    n = len(M)
    #Incognitas
    x = [0] * n
    #Matrices para LU
    s = x[::] 
    o = x[::]

    er = decompose(M,n,tol,o,s)
    if er != -1:
        substitute(M,o,n,b,x)
    return x


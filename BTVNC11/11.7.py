L=[1,2,3,4,5]
thresh=2
def elementwise_greater_than(L,thresh):
    for x in range(0,5):
        if L[x] > thresh:
            L[x]=True
        else:
            L[x]=False    
    return L
print(elementwise_greater_than(L,thresh))
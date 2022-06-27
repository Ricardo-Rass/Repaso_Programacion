
#Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

def find_missing(numeros):
    n=len(numeros)+1
    suma=(n/2)*(n-1)
    return suma - sum(numeros)

numeros = [9,6,4,2,3,5,7,0,1]  
print(int(find_missing(numeros)))
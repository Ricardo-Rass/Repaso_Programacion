def palindromo(x):
    x = str(x)
    if x == x[::-1]:
        #return x
        print(f"es palindromo el dato - > {x}")
    else:
        print("no es") 

 
        
palindromo("ana")



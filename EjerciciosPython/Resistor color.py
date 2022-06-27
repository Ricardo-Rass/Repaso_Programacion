#My Solution
def two_fer(name):
    if len(name)>=1:
        print(f"One for {name}, one for me.")
    else:
        print(f"One for you, one for me.")   
        

#best solution

def two_fer(name="you"):
    return "One for {}, one for me.".format(name)
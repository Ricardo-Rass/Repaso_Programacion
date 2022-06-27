#FooBar
#Multiplos de 2 print "foo", multiplos de 5 "bar", multiplos de ambos "foobar"

def fizzbuzz(a,b):
    result = []
    for x in range(a, b):
        if x % 3 == 0 and x % 5 == 0:
            result.append("fizz buzz")
        elif x % 3 == 0:
            result.append('fizz')
        elif x % 5 == 0:
            result.append('buzz')
        else:
            result.append(str(x))
    return result

def main():
    print(', '.join(fizzbuzz(17,54)))

main()
   
        

def isitprime(number):
    if number <= 1: 
        return False
    elif (number == 2 ): return True
    elif (number%2 == 0):
        return False
    elif (number >= 2):
           for i in range(3,number):
               if (number%i == 0):
                   return False
    return True

try: 
    inputnumber = int(input("Enter a number: "))
except(KeyboardInterrupt):
    print("Error, did not finish entering number, please try again")
except(TypeError):
    print("Error please enter an integer number")

primes = []
for j in range (1,inputnumber+1):
    if (isitprime(j)):
        print(j, "is prime")
        primes.append(j)
    else:
        print(j, "is not prime")    
print("Primes between 1 and", inputnumber,":", primes)
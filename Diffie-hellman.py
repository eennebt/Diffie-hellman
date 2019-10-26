from __future__ import print_function

'''----------------------------------------------------------------------'''
'''                 ELIAS ENNEBT 18391679 PART 2  Diffie-Hellman         '''
import random

# Calculate the A and B keys
# Shared Prime Variables , SharedBase , Asecret , Bsecret

''' DIFFIE-HELLMAN CALCULATOR '''
def Calculate(SharedPrime, SharedBase, Asecret, Bsecret):
    print("\n --------------------------------------------------------- \n")
    print("\tPublicity Shared Varibles: \n")
    # Shared Prime Numbers
    # Shared Prime
    print("\tPublicly  Shared Prime Number: ", SharedPrime)
    # Shared Base
    print("\tPublicity Shared Base Number : ", SharedBase)
    # Calculate A key  A-Secret
    Akey = (int(SharedBase**Asecret)) % int(SharedPrime)
    print("\tAsecret Sends Over Public Chanel:  ", Akey)
    # Calculate B key B-Secret
    Bkey = (int(SharedBase**Bsecret)) % int(SharedPrime)
    # Bkey
    print("\tBsecret Sends Over Public Channel:  ", Bkey)
    print("\n\tPrivately Calculated Shared Secret:  ")
    # AShared Variables
    AsharedSecret = int(Bkey**Asecret) % int(SharedPrime)
    # ASharedSecret
    print("\tUser  A Shared Secret and The Key is: ", int(AsharedSecret))
    # BSharedSecret
    BSharedSecret = int((Akey**Bsecret)) % int(SharedPrime)
    print("\tUser B Shared Secret and The Key is :  ", int(BSharedSecret))
    print("\n ---------------------------------------------------------- \n")
    return







''' COMPUER GENERATED INPUT  '''
def ran():
    # Random Variables

    # Finds a random prime number
    SharedPrime = randomPrimeNum(100)  # p

    # Find the co prime of that number
    SharedBase = randomPrimeNum(SharedPrime) # g

    #any random number 1 and 100 for the secrets
    Asecret = random.randint(1, 100) # a
    Bsecret = random.randint(1, 100) # b

    # Calculate function
    Calculate(SharedPrime, SharedBase, Asecret, Bsecret)
    return

# Random Generation of Prime Number
def ISPRIME(Number):
    # Randomly Generates Prime Number
    if Number > 1:
        # if not prime Return False
        for number in range(2, Number//2):
            if (Number % number) == 0:
                print(Number , " is not a prime Number Regenerate")
                print(number , " * ", Number//number, " = ", number)
                return False
        else: # Else if prime return Prime Number
            print(Number, " Is a Prime number ")
            return Number

    else: # if not prime Number are searches
        print(Number, " Is not a prime Number Regenerating ")
        return False

# Search and Checks for  Prime Number
def randomPrimeNum(num):
    while(True):
        try:
            Number = random.randint(2, num)
            if(ISPRIME(Number) == False): # if false continue
                print("going Again")
                continue
            else:
               return ISPRIME(Number)
        except ValueError:
            continue

''' USER GENERATED INPUT   '''

def user():
    while True:
        try:
            # User Variables
            # p
            SharedPrime = int(input("Please enter a Shared Prime Number,  p:"))
            # validate user is using a Prime user
            Sharedprime = int(uservalid(SharedPrime))
            # g
            SharedBase = int(input("Please enter a Shared Base Prime Number  g:"))
            # validate user is using a Prime user
            Sharedbase = int(checkCoPrime(SharedBase, Sharedprime))
            print(Sharedbase)
            # Asecret
            Asecret = int(input("Please enter A Asecret a K value: "))
            # Bsecret
            Bsecret = int(input("Please enter B Bsecret b K value: "))
        except ValueError:
            print("Not an Integer! Try again. ")
            continue
        else:
            return Calculate(Sharedprime, Sharedbase, Asecret, Bsecret)


 # UserValididation Function
def uservalid(num):

    while (True):
        try:
            # User is using a prime number
            ISPRIME(num)
            # if false Retry
            if (ISPRIME(num) == False):
                print("Error: Try again")
                num = int(input("Please enter Shared value Again!  "))  # p
                return ISPRIME(num)
            else:
                return ISPRIME(num)
        except ValueError:
           break
#USER CHECK CO PRIME FUNCTION
def checkCoPrime(SharedBase, SharedPrime):
    if (SharedBase > SharedPrime):
        print("try again!")
        SharedBase = int(input("Please enter Shared value Again!  "))  # p
        return uservalid(SharedBase)
    else:
        return uservalid(SharedBase)





''' MAIN    '''
def main():
    random.seed(1000)
    while(True):
        # Choices random or user input
        try:
            print("\n please enter: \n"
                  " a: random input \n"
                  " b: user input \n"
                  " c: EXIT \n ")
            x = str(input())
            if(x == "a"):
                ran() # Random() Generated
            elif (x == "b"):
                user() # User() Generated
            elif (x == "c"):
                exit()
                break
            else:
                print("Incorrect Input try again ..... \n")
        except ValueError:
            continue




if __name__ == '__main__':
    main()

'''----------------------------------------------------------------------'''
'''                 ELIAS ENNEBT 18391679 PART 2  Diffie-Hellman         '''
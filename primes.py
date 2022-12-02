"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    if number_of_primes <= 0:
        raise ValueError
    else:
        currentNumber = 2
        while len(list) != number_of_primes:
            print(currentNumber)
            prime = True
            numToDiv = 2
            while prime and numToDiv < 10:
                if currentNumber == numToDiv:
                    numToDiv += 1
                    continue
                elif currentNumber % numToDiv == 0:
                    prime = False
                numToDiv += 1

            if prime:
                print("append " + str(currentNumber))
                list.append(currentNumber)

            currentNumber += 1

    print(list)
    return list

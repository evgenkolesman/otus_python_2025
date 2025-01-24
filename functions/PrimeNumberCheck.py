import math

def prime_number_check(number):
        try:
            val = int(number)
            sqrt = math.sqrt(val)
            if val <= 1 or int(sqrt) < 2:
                print("NOT A PRIME NUMBER")
                return

            for a in range(2, sqrt):
                if(val % a == 0):
                    print("PRIME NUMBER !!!")
                    break

            else: print("NOT A PRIME NUMBER")

        except:
            print ("BAD DATA NEED NUMBER")

value = input(" Enter a number: ")

prime_number_check(value)
class AgeError(Exception):
    pass

class lessage(AgeError):
    def __init__(self):
        print("Age is less than 21 :(")

class happiness:
    def calculator(self, age):
        print("Happiness Calculator :)")
        
        if age < 21:
            raise lessage
        income = int(input("Income >> "))
        happiness = income / age
        print("For age " + str(age) + " your")
        print("happiness is " + str(happiness))

try:
    h = happiness()
    h.calculator(20)

except lessage as e:
    print(e)

import string 
class Polynomial:
    def __init__(self, firstCoefficient, firstPower, secondCoefficient, secondPower):
        self.firstCoefficient = firstCoefficient
        self.firstPower = firstPower
        self.secondCoefficient = secondCoefficient
        self.secondPower = secondPower

    def string(self):
        return (f"{self.firstCoefficient} x ^ {self.firstPower} {self.secondCoefficient} x ^ {self.secondPower}")


def subtractPolynomials(top: Polynomial, bottom: Polynomial):
    return Polynomial(top.secondCoefficient - bottom.secondCoefficient, currentPower, coefficients[i], currentPower - 1)

def findRemainder(top: Polynomial, bottom: Polynomial):
    return top.secondCoefficient - bottom.secondCoefficient


highestPower = int(input("What's the highest power of x? "))
currentPower = highestPower
coefficients = list()

for i in range(highestPower + 1):
    coefficient = int(input("Coefficient: "))
    coefficients.append(coefficient)

divCoefficient = int(input("div coefficient: "))
divConstant = int(input("Div constant: "))

currentNumerator = Polynomial(coefficients[0], currentPower, coefficients[1], currentPower- 1)

working = True
i = 0
result = ""

while working:
    resultCoefficient = currentNumerator.firstCoefficient / divCoefficient
    resultPower = currentPower - 1
    result += f"{resultCoefficient} x ^ {resultPower} + "

    i += 1
    currentPower -= 1

    top = Polynomial(resultCoefficient, currentPower, coefficients[i], currentPower - 1)
    bottom = Polynomial((resultCoefficient * divCoefficient), currentPower, resultCoefficient * divConstant, currentPower - 1)

    if currentPower != 0:
        currentNumerator = subtractPolynomials(top, bottom)

    else:
        working = False
        print()
        print("Remainder = " + str(findRemainder(top, bottom)))

stringsToRemove = ["x ^ 0 +", " ^ 1", "+ -"]

formattedResult = ((result.replace(stringsToRemove[0], "")).replace(stringsToRemove[1], "")).replace(stringsToRemove[2], "-")

print(formattedResult)
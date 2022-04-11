import string


class Binomial: #class to store two term polynoimals
    def __init__(self, firstCoefficient, firstPower, secondCoefficient,
                 secondPower):
        self.firstCoefficient = firstCoefficient
        self.firstPower = firstPower
        self.secondCoefficient = secondCoefficient
        self.secondPower = secondPower

    def string(self):
        return (
            f"{self.firstCoefficient} x ^ {self.firstPower} {self.secondCoefficient} x ^ {self.secondPower}"
        )


def subtractPolynomials(top: Polynomial, bottom: Polynomial):
    return Polynomial(top.secondCoefficient - bottom.secondCoefficient,
                      currentPower, coefficients[i], currentPower - 1)


def findRemainder(top: Polynomial, bottom: Polynomial):
    return top.secondCoefficient - bottom.secondCoefficient


highestPower = int(input("What's the highest power of x? "))
currentPower = highestPower
coefficients = list()

alphabet = string.ascii_lowercase

model = "Your equation should be in the form: ("

for i in range(highestPower):
    model += f"{alphabet[i]}x^{highestPower - i} + "

model += f"{alphabet[highestPower]})/({alphabet[highestPower+1]}x + {alphabet[highestPower+2]})"

print(model)

for i in range(highestPower + 1):
    coefficient = int(input(f"{alphabet[i]}: "))
    coefficients.append(coefficient)

divCoefficient = int(input(f"{alphabet[highestPower + 1]}: "))
divConstant = int(input(f"{alphabet[highestPower+2]}: "))

currentNumerator = Polynomial(coefficients[0], currentPower, coefficients[1],
                              currentPower - 1)

working = True
i = 0
result = ""

while working:
    resultCoefficient = currentNumerator.firstCoefficient / divCoefficient
    resultPower = currentPower - 1
    result += f"{resultCoefficient} x^{resultPower} + "

    i += 1
    currentPower -= 1

    top = Polynomial(resultCoefficient, currentPower, coefficients[i],
                     currentPower - 1)
    bottom = Polynomial((resultCoefficient * divCoefficient), currentPower,
                        resultCoefficient * divConstant, currentPower - 1)

    if currentPower != 0:
        currentNumerator = subtractPolynomials(top, bottom)

    else:
        working = False
        print()
        print("Remainder = " + str(findRemainder(top, bottom)))

stringsToRemove = ["x^0 +", "^1", "+ -"]

formattedResult = ((result.replace(stringsToRemove[0], "")).replace(
    stringsToRemove[1], "")).replace(stringsToRemove[2], "-")

print(formattedResult)

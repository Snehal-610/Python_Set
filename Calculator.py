# 2. Create a script/program that will take arguments as 1,2,3,4,5, or 6 and will also
# take operands as arguments based on the selection made it will perform the
# operation and print the result.
# • 1=Addition, 2=Subtraction, 3=Multiplication, 4=Division, 5=Exponent,


def main():
    Choice = int(input('''--------------Please Select Arithmetic Operation--------------
1. Addition:\n2. Subtraction:\n3. Multiplication:\n4. Division:\n5. Exponent\n6. Floor Division
Please Enter your Choice hear: '''))

    def Add(N1, N2, N3):
        addition = lambda x, y, z: x + y + z
        return f"Addition is: {addition(N1, N2, N3)}"

    def Sub(N1, N2, N3):
        Subtraction = lambda x, y, z: x - y - z
        return f"Subtraction is: {Subtraction(N1, N2, N3)}"

    def Mul(N1, N2, N3):
        Multiplication = lambda x, y, z: x * y * z
        return f"Multiplication is: {Multiplication(N1, N2, N3)}"

    def Div(N1, N2):
        Division = lambda x, y: x / y
        return f"Division is: {Division(N1, N2)}"

    def Exp(N1, N2):
        Exponent = lambda x, y: x ** y
        return f"Exponent is: {Exponent(N1, N2)}"

    def Flr(N1, N2):
        FloorDiv = lambda x, y: x // y
        return f"Exponent is: {FloorDiv(N1, N2)}"

    if Choice > 0 and Choice < 4:
        Number1 = int(input("Enter First numbers: "))
        Number2 = int(input("Enter Second numbers: "))
        Number3 = int(input("Enter Third numbers: "))
        if Choice == 1:
            result = Add(Number1, Number2, Number3)
            print(result)

        elif Choice == 2:
            result = Sub(Number1, Number2, Number3)
            print(result)
        elif Choice == 3:
            result = Mul(Number1, Number2, Number3)
            print(result)

    elif Choice > 3 and Choice < 7:
        Number1 = float(input("Enter First numbers: "))
        Number2 = float(input("Enter Second numbers: "))
        if Choice == 4:
            result = Div(Number1, Number2)
            print(result)
        elif Choice == 5:
            result = Exp(Number1, Number2)
            print(result)
        elif Choice == 6:
            result = Flr(Number1, Number2)
            print(result)
    else:
        return "Invalid argument"


main()

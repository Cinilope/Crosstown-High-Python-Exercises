


def doAdd(n1, n2):
    return n1 + n2

#TODO: implement the methods
def doSub(n1, n2):
    pass


def doMul(n1, n2):
    pass


def doDiv(n1, n2):
    pass


# Todo Create doMod Function the returns x1 % x2


def main():
    print("Welcome to this Calculator")

    # this is input handling
    n1 = float(input("first number is : "))
    operation = input("opertation +-*/%: ")
    n2 = float(input("second number is : "))

    result = None

    if operation == "+":
        result = doAdd(n1, n2)
    elif operation == "-":
       print("make me, Mom")
    elif operation == "*":
        print("HaHA I don't work for free! ")
    elif operation == "/":
        print(" I wont do it!!!")
    elif operation == "%":
        #result = doMod(n1, n2)
        print("create the method Dummy ")
    else:
        print("You Stupid!!")

    print(str(n1) + " " + operation + " " + str(n2) + " = " + str(result))


if __name__ == "__main__":
    main()

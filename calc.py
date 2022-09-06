def doAdd(n1, n2):
    return n1 + n2
def doSub(n1, n2):
    return n1-n2
def doMul(n1, n2):
    return n1 * n2
def doDiv(n1, n2):
    return n1/ n2
def doMod(n1, n2):
    return n1 % n2


def main():
   print("Welcome to this Calculator")
   n1 = float(input("first number is : "))
   operation = input("opertation +-*/%: ")
   n2 =  float(input("second number is : "))
   result = None
   if operation ==  "+":
    result = doAdd(n1,n2)
   elif operation == "-":
     result =  doSub(n1, n2)
   elif operation ==  "*":
     result = doMul(n1,n2)
   elif operation == "/":
       result = doDiv(n1, n2)
   elif operation == "%":
     result = doMod(n1, n2)
   else:
    print("You Stupid!!")
   print(str(n1)+ operation + str(n2) + "= " + str(result))
if __name__ == "__main__":
    main()
def getTriangle(value):
    tot = 0
    for i in range(int(value)):
        tot = tot + i
    return tot
def getFact(value):
    tot = 1
    for i in range(1,int(value)+1):
        tot = tot * i
    return tot


def main():
    valueTri = input("input number to  Triangle: ")
    print(str(getTriangle(valueTri)))

    valueFact = input("input number to  Fact: ")
    print(str(getFact(valueFact)))

if __name__ == "__main__":
    main()
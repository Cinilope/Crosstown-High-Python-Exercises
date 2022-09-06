
from itertools import permutations
import random
import time

def encript(inputString):
    strlst = list(inputString)
    for i  in range(len(inputString)):
        j =  random.randrange(0,i+1)
        strlst[i], strlst[j] = strlst[j], strlst[i]
        "".join(strlst)
    outputStr = ""
    return  outputStr.join(strlst)


def decript(inputString):
    return [''.join(p) for p in permutations(inputString)]

def main():
    start_time = time.time()
    f = open("C:/Users\k1tut\AppData\Roaming\JetBrains\PyCharmCE2020.2\scratches\SecretPasssword.txt", "r")
    pword = f.read()
    encripedPword =  encript(pword)
    print("password " + encripedPword)
    for perm in decript(encripedPword):
        print(perm +" is " + pword + " " + str(perm == pword))
        if perm == pword:
            print(perm + " is " + pword + " " + str(perm == pword))
            break
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
import copy
def wrongnum(sodoko , satr , soton , adad , square):
    if adad in sodoko[satr]:
        return True
    for i in sodoko:
        if i[soton] == adad:
            return True
    satrc = satr // square
    sotonc = soton // square
    satr = satrc * square
    soton = sotonc * square
    while satr//square == satrc:
        while soton//square == sotonc:
            if sodoko[satr][soton] == adad:
                return True
            soton += 1
        soton = sotonc * square
        satr += 1
    return False

def isnull (sodoko):
    ans = False
    for i in range(len(sodoko)):
        if (None in sodoko[i]):
            return True
    return ans

def sodokoprint (sodoko):
    for i in range (len(sodoko)):
        for j in range (len(sodoko[1])):
            if sodoko[i][j] != None:
                print(sodoko[i][j],end = " ")
            else:
                print("-" , end = " ")
        print()

def sodokoInput (sodoko,bigest,square):
    sotonlen = len(sodoko[0])
    satrlen = len(sodoko)
    backup = copy.deepcopy(sodoko)
    while (isnull(sodoko)):
        sodokoprint(sodoko)
        action = str(input("action :"))
        if action != "delete" and action != "add":
            print("invalid input")
            continue
        satr = int(input("satr :"))
        if satr > satrlen:
            print("invalid input")
            continue
        satr -= 1
        soton = int(input("soton :"))
        if soton > soton:
            print("invalid input")
            continue
        soton -= 1
        if action == "add":
            adad = int(input("adad :"))
            if adad > bigest or adad < 1:
                print("invalid Number")
                continue
            elif wrongnum(sodoko , satr , soton , adad , square):
                print("this num cant be added in here")
                continue
            elif sodoko[satr][soton] == None:
                sodoko[satr][soton] = adad
            else:
                print("place is full")
        else:
            if backup[satr][soton] == None:
                sodoko[satr][soton] = None
            else:
                print("you cant delet this num!")
                
    sodokoprint(sodoko)

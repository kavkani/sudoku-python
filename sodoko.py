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

def sodokoInput (sodoko,bigest):
    sotonlen = len(sodoko[0])
    satrlen = len(sodoko)
    while (isnull(sodoko)):
        sodokoprint(sodoko)
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
        adad = int(input("adad :"))
        if adad > bigest or adad < 1:
            print("invalid Number")
            continue          
        if sodoko[satr][soton] == None:
            sodoko[satr][soton] = adad
        else:
            print("place is full")
            
        

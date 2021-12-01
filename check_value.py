import audio_procces
import audio_input
import copy
def wrongnum(sodoko, satr, soton, adad, square):
    if adad in sodoko[satr]:
        return True
def sodokoInput(sodoko, bigest, square):
    sotonlen = len(sodoko[0])
    satrlen = len(sodoko)
    backup = copy.deepcopy(sodoko)
    '''while (isnull(sodoko)):
        sodokoprint(sodoko)
        action = str(input("action :"))
        if action != "delete" and action != "add":
            print("invalid input")
            continue'''
        satr = int(input("satr :"))
        if satr > satrlen:
            print("invalid input")
            continue
        soton -= 1
        if action == "add":
            print("say a number :", end=" ")
            adad = int(audio_procces.procces('output.wav'))
            print(adad)
            if adad > bigest or adad < 1:
                print("invalid Number")
                continue
            elif wrongnum(sodoko, satr, soton, adad, square):
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
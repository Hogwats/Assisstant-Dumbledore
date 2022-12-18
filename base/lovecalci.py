from base.general import *


# def flames_meaning(result):

#             switcher = {
#                 'F': 'Friendship',
#                 'L': 'Love',
#                 'A': 'Affection',
#                 'M': 'Marriage',
#                 'E': 'Enemy',
#                 'S': 'Sweetheart'
#             }
            
#             return switcher.get(result)


# def flames(name1, name2):

#             flames = 'FLAMES'

#             for x in name1:
#                 if x in name2:
#                     name2 = name2.replace(x, '', 1)
#                     name1 = name1.replace(x, '', 1)

#             flamed_name = name1 + name2

#             print('\nFlamed name >>> ' + flamed_name)

#             flamed_name_length = len(flamed_name)

#             print('\nComputing FLAMES...')

#             print('\nNow ' + flames)

#             while len(flames) != 1:

#                 if len(flames) >= flamed_name_length:
#                     striked_out_char = flames[flamed_name_length - 1]
#                     flames = flames.replace(striked_out_char, '', 1)

#                 else:
#                     striked_out_char = flames[(flamed_name_length % len(flames)) - 1]
#                     flames = flames.replace(striked_out_char, '', 1)

#                 print('Now ' + flames + ', striked out ' + striked_out_char)

#             print('\nFLAMES result: ' + flames_meaning(flames))

# def result():
#     speak("Please Enter Your  Name ")
#     youname = str(input("Please Enter Your Name : "))
#     speak("Enter Your Life Partner Name ")
#     crushname = str(input("Please Enter Your Crush Name :"))    
#     speak(flames_meaning(flames(youname,crushname)))

# result()



# function for removing common characters  
def eliminateCommonChars(listOne, listTwo) :  
    for i in range(len(listOne)) :  
        for j in range(len(listTwo)) :  
            if listOne[i] == listTwo[j] :  
                c = listOne[i]  
                listOne.remove(c)  
                listTwo.remove(c)  
                listThree = listOne + ["*"] + listTwo  
                return [listThree, True]  
  
    listThree = listOne + ["*"] + listTwo  
    return [listThree, False]  
  
def calculator():
            speak("Tell Your  Name ")
            # yourname = str(input("Please Enter Your Name : ")) 
            yourname = takeCommand()
            yourname = yourname.lower()  
            yourname.replace(" ", "")  
            yournameList = list(yourname)  
        
            speak("Tell Your Life Partner Name ")
            # crushname = str(input("Please Enter Your Crush Name :"))    
            crushname = takeCommand()
            crushname = crushname.lower()  
            crushname.replace(" ", "")  
            crushnameList = list(crushname)  
        
            proceed = True  
            
            while proceed :  
                retList = eliminateCommonChars(yournameList, crushnameList)  
                conList = retList[0]  
                proceed = retList[1]  
                starIndex = conList.index("*")  
        
                yournameList = conList[ : starIndex]  
                crushnameList = conList[starIndex + 1 : ]  
        
            theCount = len(yournameList) + len(crushnameList)  
        
            # list of FLAMES acronym  
            res = ["Friends", "Lovers", "Affectionate", "Marriage", "Enemies", "SweetHeart"]  
        
            while len(res) > 1 :  
                splitIndex = (theCount % len(res) - 1)  
                if splitIndex >= 0 :  
                    right = res[splitIndex + 1 : ]  
                    left = res[ : splitIndex]  
                    res = right + left  
                else :  
                    res = res[ : len(res) - 1]  
        
            # print final result  
            print(" Your Relationship Status ")
            print(res[0])
            speak(" Your Relationship Status ")
            speak(res[0])
def result():
    speak('welcome To Love Calculator')
    calculator()


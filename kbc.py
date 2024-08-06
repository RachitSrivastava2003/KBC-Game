import random
import time
import os
print("\n\n->->->->->->->->->->->->->-> KON BANEGA COREPATI GAME <-<-<-<-<-<-<-<-<-<-<-<-<-<-<-\n\n")
a=input("Press(1) START\nPress(2) EXIT\n\nEnter:")
if(a=="1"):
    # List To store Qusetion Answer And prize For easy 
    question=["\nQ.Who Is The First Prime Minister Of India?\n(a)Jawah Lal Nehru\t(b)Narendra Modi\n(c)Mahatma Gandhi\t(d)Rabindra Nath Tagore\n","\nQ.National Bird Of India?\n(a)Peacock\t(b)Sparrow\n(c)Owl\t(d)Kingfisher\n","\nQ.National Animal Of India?\n(a)Tiger\t(b)Lion\n(c)Cow\t(d)Rihno\n","\nQ.For which of the following disciplines is Nobel Prize awarded?\n(a)Physics and Chemistry\t(b)Physiology or Medicine\n(c)Literature,Peace and Economics\t(d)All of the above\n","\nQ.National Bird Of India?\n(a)Peacock\t(b)Sparrow\n(c)Owl\t(d)Kingfisher\n","\nQ.he gas usually filled in the electric bulb is?\n(a)nitrogen\t(b)hydrogen\n(c)carbon dioxide\t(d)oxygen\n","\nQ.Which of the following is used in pencils?\n(a)Graphite\t(b)Silicon\n(c)Charcoal\t(d)Phosphorous\n","\nQ. Chemical formula for water is?\n(a)NaAlO2\t(b)H2O\n(c)Al2O3\t(d)CaSiO3\n"]
    answer=["a","a","a","d","a","a","a","b"]
    prize=["500","1500","2500","5000","10000","25000","50000","100000"]
    l=len(question)     #length of question use for while to operate 
    i=0
    f=0
    while(i<l):
        os.system('cls')  # Use To Clear Cmd For Next Question 
        t="Total Amount: "
        print(t.center(10),f)
        a=("\n\n------------------ KON BENEGA COREPATI ----------------------\n\n")
        print(a.center(50))
        que=question[i]
        # que=random.choice(question) 
        print("Winning Amount : ",prize[i],"\n",que)
        b=question.index(que)   
        d=answer[b]
        c=input("Enter Option: ")
        if c==d:         # If value Of C And D Is equal Then It Enter In If Condition
            print("\n\t\tCorrect Answer\n")
            print("You Won",prize[i],"/-Rs\n")
            print("Your Next Question is coming........\t")
            f=f+int(prize[i])
            i=i+1  
            for x in range(3,0,-1):
                print(x)
                time.sleep(1)    # Use this To Stop for 1 Sec To Showing That Next Question Is coming
        elif(c!=d):
                print("\n\t\tOhoo!! Wrong Answer\n")
                print("Congratulation !! You Won",f,"/-\n")
                print("Amount Transfering To Your Bank..............\n")
                time.sleep(3)
                print("Successfully Desposited !!\n")
                time.sleep(6)
                print("\n\t\t\tThank You For Playing KBC !!")
                break
# if all question is completed then it goes into this condition
    if(i>=l):
      os.system('cls')
      print("You Completed All Level Of Game, hurraah !!\n\n")    
      time.sleep(2)
      print("Congratulation !! You Won",f,"/-\n")
      print("Amount Transfering To Your Bank..............\n")
      time.sleep(3)
      print("Successfully Desposited !!\n")
      time.sleep(6)
      print("\n\t\t\tThank You For Playing KBC !!")
elif(a=="2"):
     print("\t\t\tThank You For Playing KBC !!")
else:
     print("\n\tInvalid Choice :(")
     exit()     

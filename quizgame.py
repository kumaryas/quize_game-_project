import random
import time
#print * 80 times
for i in range(80):
    print("*",end="")
    time.sleep(0)

print()
print("\t\t\t Welcome to")
print("\t\t\t QUIZ GAME")
for i in range(80):
    print("*",end="")
    time.sleep(0)
print()
a=input("\tEnter Your Name - ")
for i in range(80):
    print("*",end="")
    time.sleep(0)
print()
print("\n\t\tOK ",a,"chalo suru krte h game yash question puch")
time.sleep(1)
questions=["Which one is the first fully supported 64-bit operating system","Computer Hard Disk was first introduced in 1956 by","Which of the following is not a web browser","In computer world. Trojan refer to","Which one of the followings is a programming language","Which protocol is used to received e-mail","Which protocol is used to send e-mail","Which computer program converts assembly language to machine language","In which year @ sign was first chosen for its use in e-mail address","Which one is the latest one from PARAM SuperSries computers","Who is also know as the father of Indian Supercomputing","A folder in windows computer can't be made with the name"]
answer=["Linux","IBM","Facebook","Malware","HTML","POP3","SMTP","Assembler"," 1972"," PARAM Yuva II","Vijay Bhatkar"," con"]
wronganswers=[[" Windows Vista","Mac","Windows XP"],["Dell","Apple","Microsoft"],["MOSAIC"," www"," Netscape navigator"],["Virus","Worm","Spyware"],[" HTTP"," HPML"," FTP"],[" SMTP","HTTP","FTP"],["HTTP","POP3"," SSH"],["Interpreter","Compiler","Comparator"],["1976","1980"," 1977"],["PARAM 10000"," PARAM Padma","PARAMnet"],[" Ragunath Mashelkar"," Jayant Narlikar","Nandan Nilekani"],["can","mak"," make"]]
attempquestion=[]
count=1
point=0
while True:
    while True:
        selectquestion=random.choice(questions)
        if selectquestion in attempquestion:
            pass
        elif selectquestion not in attempquestion:
            attempquestion.append(selectquestion)
            questionindex=questions.index(selectquestion)
            correctanswer=answer[questionindex]
            break
    optionslist=[]
    inoptionlist=[]
    optioncount=1
    while optioncount<4:
        optionselection=random.choice(wronganswers[questionindex])
        if optionselection in inoptionlist:
            pass
        elif optionselection not in inoptionlist:
            optionslist.append(optionselection)
            inoptionlist.append(optionselection)
            optioncount+=1
    optionslist.append(correctanswer)
    alreadydisplay=[]
    optiontodisplay=[]
    a1=True
    while a1:
        a=random.choice(optionslist)
        if a in alreadydisplay:
            pass
        else:
            alreadydisplay.append(a)
            optiontodisplay.append(a)
            a1=not True
    a1=True
    while a1:
        b=random.choice(optionslist)
        if b in alreadydisplay:
            pass
        else:
            alreadydisplay.append(b)
            optiontodisplay.append(b)
            a1=not True
    a1=True
    while a1:
        c=random.choice(optionslist)
        if c in alreadydisplay:
            pass
        else:
            alreadydisplay.append(c)
            optiontodisplay.append(c)
            a1=not True
    a1=True
    while a1:
        d=random.choice(optionslist)
        if d in alreadydisplay:
            pass
        else:
            alreadydisplay.append(d)
            optiontodisplay.append(d)
            a1=not True
    right_answer=""
    if correctanswer==a:
        right_answer="a"
    elif correctanswer==b:
        right_answer="b"
    elif correctanswer==c:
        right_answer="c"
    elif correctanswer==d:
        right_answer="d"
    print("--------------------------------------------------------------------------------------------")
    print("\t\t\tpoints- ",point)
    print("--------------------------------------------------------------------------------------------")
    time.sleep(1)
    print("\n\t\tQuestion ",count,"chalo batao ")
    print("--------------------------------------------------------------------------------------------")
    time.sleep(1)
    print("  |  Question - ",selectquestion)
    print("--------------------------------------------------------------------------------------------")
    print("\t-----------------------------------------------------------------------------")
    time.sleep(1)
    print("\t|  A. ",a)
    print("\t-----------------------------------------------------------------------------")
    time.sleep(1)
    print("\t|  B. ",b)
    print("\t-----------------------------------------------------------------------------")
    time.sleep(1)
    print("\t|  C. ",c)
    print("\t-----------------------------------------------------------------------------")
    time.sleep(1)
    print("\t|  D. ",d)
    print("\t-----------------------------------------------------------------------------")
    useranswer=input("\t\tanswer\t   or \t press Q to quit.\n\t\t\t...").lower()
    if useranswer==right_answer:
        if count==1:
            point=10
        elif count==2:
            point=20
        elif count==3:
            point=30
        elif count==4:
            point=40
        elif count==5:
            point=50
        elif count==6:
            point=60
        elif count==7:
            point=70
        elif count==8:
            point=80
        elif count==9:
            point=90
        elif count==10:
            point=100
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("*********************************************************************************")
            print("\t\t\t \\\\\\\\\\ Congratulations! //////////")
            print("\t\t\t|||||||||| You Won The Game ||||||||||")
            print("*********************************************************************************")
            print("\n\n\t\t You Won  ",point)
            print()
            break
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("*********************************************************************************")
        print("\t\t\t \\\\\\\\\\ Congratulations! //////////")
        print("\t\t\t|||||||||| Right Answer ||||||||||")
        print("*********************************************************************************")
        count+=1
    elif useranswer=="q":
            print("\n\n\t\t You Won  ",point)
            break
    else:
        print("*********************************************************************************")
        print("\t\t\tWrong Answer")
        print("*********************************************************************************")
        print("\n\n\t\t \tYou Won  ",point)
        print("*********************************************************************************")

        break

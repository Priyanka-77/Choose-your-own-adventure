name = input("Enter your name: ")
print("Welcome", name, "in Adventure Game!!")

ques1 = input("You are in middle of road b/w left and right. Type which one you choose to continue your journey: ").lower()
if ques1 == "left":
    ques1 = input("You are alive, now continue by choosing again b/w bike or boat: ")
    
    if ques1 == "bike":
        ques1 = input("Drive straight then make you turn, by passing hurdles then choose partner b/w girl or boy: ")
        if ques1 == "girl":
            print("She is mobester, she shot you by gun, Sorry you lose!!")
        elif ques1 == "boy":
            print("You make a great team, you've shot the girl who is mobester")
            print("By killing her, you won this adventure")
        else:
            print("Type b/w girl or boy")
    
    elif ques1 == "boat":
        print("Ok, hope in it but there is a gangster who killed you")
        print("Sorry, you died by making wrong choice")
    
elif ques1 == "right":
    ques1 = input("Choose b/w knife or gun: ")
    if ques1 == "knife":
        print("You make good choice! Now, it's yours")
    elif ques1 == "gun":
        print("Sorry!, there are not bullets, you've made wrong choice")
    else:
         print("Type b/w knife or gun")
    
else:
    print("Type a valid option?")
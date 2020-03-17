import random

def windo():
	for i in range(0,50):
		print("_",end="")
	print()
	print("$",end="")
	for i in range(0,49):
		print(" ",end="")
	print("$")
	print("$",end="")
	for i in range(0,49):
		print(" ",end="")
	print("$")
	print("$",end="")
	for i in range(0,49):
		print(" ",end="")
	print("$")

	print("$",end="")
	for i in range(0,18):
		print(" ",end="")
	print("WELCOME TO GAME!!!",end="")
	for i in range(0,13):
		print(" ",end="")
	print("$")
	print("$",end="")
	for i in range(0,49):
		print(" ",end="")
	print("$")
	print("$",end="")
	for i in range(0,49):
		print(" ",end="")
	print("$")
	for i in range(0,50):
		print("_",end="")

	input("\n\nENTER ANY KEY TO START:")



def menu():
	print("1.ROCK PAPER SCISSOR\n\n 2.COWS AND BULLS\n\n3.EXIT")
	n=int(input("\nENTER ChOICE:"))
	if(n==1):
		rock()
	elif(n==2):
		cow()
	elif n==3:
		exit()
	else:
		print("\nINVALID!!!!\n")
		menu()

def rock():
	print("\n1.PLAY\n2.MENU\n")
	p=int(input("ENTER ChOUICE:\n"))
	if p==1:
		rockpaper()
	elif p==2:
		menu()
	else:
		print("INVALID !!!\n")
		rock()

def cow():
	print("\n1.PLAY\n2.MENU\n")
	c=int(input("ENTER ChOUICE:\n"))
	if c==1:
		bull()
	elif c==2:
		menu()
	else:
		print("INVALID !!!\n")
		cow()


def rockpaper():
	print("WELCOME TO THIS GAME!!")
	print("YOUR OPPONENT WILL BE COMPUTER!!!")
	print("First One To Score 5 points Willl be WINNER")
	print("ENTER 1 for RoCK:")
	print("ENTER 2 For PAPER:")
	print("ENTER 3 for SCISSOR:")
	print("ENTER 0 TO WXIT:")
	user=0
	comp=0
	count=0
	chc=['0',"ROCK","PAPER","SCISSOR"]
	while(user<5 and comp<5 and count<25):
		count+=1
		u_ch=int(input("ENTER YOUR CHOICE:"))
		if u_ch==0:
			print("Thank you for playing!!")
			break
		c_ch=random.choice([1,2,3])
		if u_ch==1 and c_ch==2:
			comp+=1
		elif u_ch==1 and c_ch==3:
			user+=1
		elif u_ch==2 and c_ch==1:
			user+=1
		elif u_ch==2 and c_ch==3:
			comp+=1
		elif u_ch==3 and c_ch==1:
			comp+=1
		elif u_ch==3 and c_ch==2:
			user+=1
		print("\nYOU:",chc[u_ch])
		print("\nCOMP:",chc[c_ch])
		print("\nSCOREs\n YOU:",user,"\nCOMP:",comp)
	if(user>comp):
		print("CONGRATSS YOU WINN!!!")
	elif(user==comp):
		print("ITS A DRAW")
	else:
		print("YOU LOST!!!BETTER LUCK NEXT TIME!!!!")
	menu()

def bull():
    print("WELCOME TO COWS AND BULLS!!!")
    print("COWS: WRONG POSITIONS ")
    print("BULLS: RIGHT POSITIONS")
    print("MAXIMUM 15 GUESSES ALLOWED")
    words=['rate','fail','help','loam','cops','soil','wire','dear','acer','bale']
    rand=random.randrange(0,10)
    word=words[rand]
    count=0
    while(count<15):
        s=input("ENTER STRING(4 letters):")
        if s=="-1":
            print("THANKN YOUN FOR PLAYING!!!")
            print("cows: no. of ")
            return
        cw=0
        bu=0
        chars=0
        for c in s:
            if c in word:
                chars+=1
        for i in range(0,4):
            if s[i]==word[i]:
                bu+=1
        cw=chars-bu
        print("cows:",cw)
        print("BULLS:",bu)
        if bu==4:
            print("CONGRATSSS!!! YOUU WINN!!!")
            menu()
        count+=1
    print("MAXIMUM LIMIT RECAHED!!! BETER LUCK NEXT TIME:")
    menu()


windo()
print("\n"*100)
menu()






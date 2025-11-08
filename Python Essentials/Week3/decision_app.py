ansyes=0
ansno=0
neg=['No','no','NO','N','n'] # No inputs
pos=['Yes','yes','YES','Y','y'] # Yes Inputs
while True:
    ans=input("<DO YOU LOVE THE CITY YOU LIVE IN? (Y/N)> ")
    if ans in pos:
     ansyes+=1 
     if ansyes==3:
      break #Skips to the end after 3 positive inputs
     print("Continuing. \nYOU\nMUST\nBECOME\nSTRONG")
    elif ans in neg:
        ansno+=1
        if ansno==3:
         break #Same as the other break, but negative
        print("Incorrect Input. \nYOU\nMUST\nBECOME\nSTRONG")
    elif ans not in [pos,neg]:
        print("Unexpected Input. \nYOU\nMUST\nBECOME\nSTRONG") #Infinite loop if the question is never answered due to the input not being in list
if ansyes==3:
    print("You are not strong enough.")
elif ansno==3:
    print("You are strong enough.")
# ignore that this is weird its based on one of my favorite games ever

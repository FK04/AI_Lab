import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word=random.choice(word_list)
display=[]

for i in range(len(chosen_word)):
   
	display.append("_")
while "_" in display:
	guess=input("Guess a letter:").lower()
	for i in range(len(chosen_word)):
 
		letter=chosen_word[i]
		 
		if letter==guess:
    
			print("correct guess")
			display[i]=letter  
		print(display)
  
		
else:
	print("You have won")
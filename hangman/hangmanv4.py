import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word=random.choice(word_list)
lives=6
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
 
	if guess not in chosen_word:
            
		lives=lives-1
            
		print(lives) 
	if lives==0:
            
		print("You loose")
            
		exit(1)
		
else:
	print("You have won")
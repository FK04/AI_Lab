import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word=random.choice(word_list)
display=[]

for i in range(len(chosen_word)):
   
	display.append("_")
guess=input("Guess a letter:").lower()
for i in range(len(chosen_word)):
  
	if guess in chosen_word[i]:
    
		print("correct guess")
		display.insert(i,guess)
    
		print(display)
  
	else:
    
		print("wrong guess")
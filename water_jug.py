a=int(input("Enter Capacity of Jug A : "))
b=int(input("Enter Capacity of Jug B : "))
ai=int(input("Enter Initial Capacity of Jug A : "))
bi=int(input("Enter Initial Capacity of Jug B : "))
af=int(input("Enter Final Capacity of Jug A : "))
bf=int(input("Enter Final Capacity of Jug B : "))

if((af>a) or (bf>b) or ( (((a+b)%2)!=((af+bf)%2)) and ( (af!=a)and(bf!=b)) ) ):
	print("No Solution Possible !")
	exit(1)

print("List OF Operations you can do :\n")
print("1.Fill Jug A Completely")
print("2.Fill Jug B Completely")
print("3.Empty Jug A Completely")
print("4.Empty Jug B Completely")
print("5.Pour from Jug A till Jug B is filled completely or A becomes empty")
print("6.Pour from Jug B till Jug A is filled completely or B becomes empty")
print("7.Pour all from Jug A to Jug B")
print("8.Pour all from Jug B to Jug A")

while((ai!=af or bi!=bf)):
	op=int(input("Enter The Operation: "))
	if(op==1):
		ai=a
	elif(op==2):
		bi=b
	elif(op==3):
		ai=0
	elif(op==4):
		bi=0
	elif(op==5):
		if(b-bi>ai):
			bi=ai+bi
			ai=0
		else:
			ai=ai-(b-bi)
			bi=b
	elif(op==6):
		if(a-ai>bi):
			ai=ai+bi
			bi=0
			
		else:
			bi=bi-(a-ai)
			ai=a
	elif(op==7):
		if(ai<a):
			bi=ai+bi
			ai=0
		else:
			print("Overflow , select another option")
	elif(op==8):
		if(bi<b):
			ai=ai+bi
			bi=0
		else:
			print("Overflow , select another option")
	print(ai,bi)

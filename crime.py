import csv    #import the csv module from python
file=open("Crime.csv",'r')  #opens the directed file
#word_list=[]
list1=[]
list2=[]		#an empty list to put all words of csv file
for line in file:
	line=line.strip() #strips the whitespaces
#	print(line)
	line= line.split(',') #splits the whole content wrt commas.
#	print(line)
	list1.append(line[-1])
	list1.append(line[-2])   #create a list of strings in table. 
#print(list1)
#print(list2)
#d=zip(list1,list2)
#print(d)
"""
for item in list1:
	count=0
	for i in range(list1):
		if list1[i]=item:
			count+=1
	print(item,count)

for i in range(len(list1)):

"""

list3=[]
for i in list2:  #counts for a particular word in the whole list 
	count=0
	for j in range(len(list2)):
		if i==list2[j]:
			count+=1  #increments the value
	list3.append(count) #modified list
print("CRIME","	"*10,"CRIME ID"," "*10,"COUNT")  #print headers of the table
for i in range(len(list1)):
	print(list1[i],"           ",list2[i],"          "list3[i])

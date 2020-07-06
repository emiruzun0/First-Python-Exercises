# -*- coding: utf-8 -*-
#string
message = "Hello World!"

print(message[:5])  #print from 5.index to end
print(message[2:5]) #print from 2.index to 5.index
newMessage = message[:9]

print(len(message)) #length of message 


#lower / upper
print(message.upper()) #upper letters
print(message.lower()) #lower letters


#replace
print(message.replace("o","u")) #replace strings 

#split and strip
sentence = "   Talk is cheap show me the code   "
print(sentence.split()) #split the sentence by whitespace
print(sentence.strip()) #Remove spaces at the beginning and at the end of the string
print(sentence.split()[3]) #Split and print the index 3

#input
name = input("Name : ")
number1 = input("Number 1 : ")
number2 = input("Number 2 :")
print(number1 + number2) #print as string
print(int(number1) + int(number2)) #sum of numbers


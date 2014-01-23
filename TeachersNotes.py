# -*- coding: utf-8 -*-
#Python Cue Cards
#Les Pounder 23rd January 2014
#Teacher's Answers

#Card 1
#This should work as per the card, there is no challenge for this card.

#Card 2
#There is no challenge for this card.

#Card 3
#There is no challenge for this card.

#Card 4
#The incorrect sum is trying to divide integers that result in an answer with a
#fraction, or decimal point.
#I use the sum 25/6 which is 4.1666. Python will show 4.
#To divide 25/6 we have to use a float so it becomes 25.0/6

#Card 5
#Python does not want to join a string and an integer (or float) together.
#They are incompatible, so we need to alter the integer and make it a string.

AgeIs =  "My age is "
age = 34

#print AgeIs + age #<<ERROR!
print AgeIs + str(age)

#Card 6
#At time of writing, £1 is equal to $1.66. $1 is also equal to £0.60
print 10.0 * 1.66

#Card 7
#We use raw_input to capture the users keyboard input.
#Any input captured this way is stored as a string, and we cannot do any maths
#with a string, so we must use a helper function called int() or float() to change
#the string to an interger or a float.

number1 = int(raw_input("Think of a number "))
number2 = int(raw_input("Think of another number "))
print "The sum of "+ str(number1) + " and " + str(number2) + " is..."
print number1 + number2

#Card 8
#There can be many outcomes to this card, so ensure that the logic is sound.

#Card 9
#There is no challenge for this card.

#Card 10
#There is no challenge for this card.

#Card 11
#Here we have the beginning of a simple game, we can expand the code to become
#a quiz.

age = int(raw_input("How old are you? "))
if age < 5:
    print "You are at nursery"
elif age < 7:
    print "You are at infants"
elif age < 10:
    print "You are at juniors"
elif age < 17:
    print "You are at secondary school"
else:
    print "You have left school"

#Card 12
#Here we can use the double equals to compare a variable against a hard coded value.
a = raw_input("Fruit? ")
b = raw_input("Fruit? ")
if a == "apple" and b == "orange":
	print "You like " + a + " and " + b
else:
    print "You do not eat fruit?"

#Card 13
#There is no challenge for this card.

#Card 14
#This loop is an infinite loop, and will continue on and on.
name = "Les"
while True:
    print "Hello"
    print name

#Card 15
#Functions are great, think of them as a powerful macro.
def myname():
    name = raw_input("What is your name? ")
    print name * 20

#Card 16
#There is no challenge for this card.

#Card 17
#We can use functions like this to do all sorts of quick little jobs.
def convert(n):
    return n * 0.60

#Card 18
#This can expand quite a bit, make sure the logic is sound and check for typos.

#Card 19
#Modules provide lots of extra functionality to your Python code.
import time
name = "Les"
while True:
    time.sleep(2)
    print "Hello"
    time.sleep(2)
    print name

#Card 20
#Turtle is a great way to demonstrate loops and iteration in a graphical manner
from turtle import *
for i in range(20,41):
    circle(i)

#Card 21
#The quickest way to do this is via a for loop, as we need to print list[x]
#where x is the index number of the item in the list. 
list = ["Apple","Banana","Orange"]
for item in list:
    print item

#Card 22
while True:
	print "Les \n" * 20
	break

#Card 23
#We can choose our fruit from the list that we created in card 21.

fruit = random.choice(list)
print "You should really eat more " + fruit

###END OF CARDS###
lespounder@gmail.com

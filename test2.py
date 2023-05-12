#gst calculator
"""itemprice = 250
gst = 7/100
total = (itemprice * gst) + itemprice
print(total)"""

#mark calculator
"""c = float(input("Enter common test mark:"))
a = float(input("Enter assignment mark:"))
ca = float(input("Enter continuous assessment mark:"))
common = c * (30/100)
assignment = a * (30/100)
CA = ca * (40/100)
final = CA + assignment + common
print("Your finalmark is",final)"""

#enhanced version of mark calculator
"""sn = str(input("Enter student number:"))
c = float(input("Enter common test mark:"))
a = float(input("Enter assignment mark:"))
ca = float(input("Enter continuous assessment mark:"))
common = c * (30/100)
assignment = a * (30/100)
CA = ca * (40/100)
final = CA + assignment + common
print()
print('{:11s} {:7s} {:7s} {:10s} {:7s}'
      .format ('StudentNo','Test','Assgn','CA','Final'))
print('{:<11s} {:<7.2f} {:<7.2f} {:<10.2f} {:<7.2f}'.format(sn,c,a,ca,final))"""
 
#time converter
"""sec = input("Time in seconds:")
hr = int(sec)// 3600
mins = (int(sec) % 3600)//60
secs = (int(sec) % 3600)%60
print(int(hr),"hr(s)",mins,"min(s)",secs, "s")"""

#integer sqaure
"""num = input("enter an integer:")
def square(num):
    if not num.isdigit():
        return"invalid entry"
    num = int(num)
    return num * num
print(num, "squared is", square(num))"""

#formatting exercise
"""print('{:6s} {:6s} {:15s}' .format("a","b","a to the power of b"))
a = 1
b = 2
while a < 6 and b < 7:
    print('{:<6d} {:<6d} {:<15d}' .format(a,b, a**b))
    a += 1
    b += 1"""

#importing functions, related to cat.py 
"""import cat
cat.purr("abc")
cat.lick("abc")
cat.nap("jg")"""

#function
"""def hello():
  name = str(input("Enter your name: "))
  if name:
    print ("Hello " + str(name))
  else:
    print("Hello World") 
  return"""

#modifying strings
"""message = "Welcome to ICT"
print(message[10])
print(len(message))
#print(message[22])<- IndexError: string index out of range
print(message.find("ICT"))
print(message[11:14])
print(message.replace("e","r",1))
print(message.replace("ICT","NP"))
print("NP" in message)
print(message.upper())
print(message.capitalize())
print(message.lower())"""

#joining strings
"""s1 = "Programming 1"
s2 = "PRG1"
s1 = s1 +" "+ s2
print(s1)"""

#some list thing
"""s3 = '10;20;30'
index = s3.find(';')
print(index) # index no.2
print(s3[0:index])# [0:2] -> prints characters at indexes 0 and 1 
temp = s3[index+1:] #s3[3:] characters at index no.3,4,5,6....all the way to the last one
print(temp)#temp is a new list, temp = [20:30]
print(temp[0:index]) #temp[0:3]"""

#string removal
"""original = input("Enter original string:")
sub = input("Substring to delete:")
delete = original.replace(sub,"",1)
print("The modified string is:", original)"""
#another method
"""original_str = input("Enter original string: ")
substring = input("Enter substring to delete: ")
index = original_str.find(substring)
left_str = original_str[:index]
right_str = original_str[index +len(substring):]
new_str = left_str + right_str
print('\nThe modified string is: {}'.format(new_str))"""

#number list
"""markslist = [89,77,55,69,50,60,11,10,14,20]
print(markslist)
print("The 1st element is" , markslist[0])
sums = int(markslist[-1]) + int(markslist[-2])
print("The sum of the last 2 elements is", str(sums))
double = markslist[1] * 2
print("Double value of 2nd element is", double)"""

#name list
"""nameList = ["Tom","Joe","Mary","John","Bob","Jane"]
search = str(input("Enter name to search:"))
if search in nameList:
    print("Name {} is found in position".format(search),nameList.index(search),"in the nameList")
else:
    print("Name {} is not found in the namelist".format(search))"""

#commission calculator
"""sales = int(input("Enter the monthly sales of sales agent:"))
if sales >= 10000:
    commission = 10
    commission_earned = sales * (commission/100)

else:
    commission = 5
    commission_earned = sales * (commission/100)

print("The commission rate is {}%".format(commission))
print("The commission earned: {}".format(commission_earned))"""

#simple addition  
"""import random
num1 = random.randint(0,100)
num2 = random.randint(0,100)
total = num1 + num2   
x = input("Enter the sum of %s and %s:"%(num1 , num2))
if not x.isdigit():
    print("Invalid! Enter only integers.")
elif x != str(total):
    print("Your answer is wrong. \nThe correct answer is %s."%(total))
else:
    print("Your answer is correct!")"""

#number guessing game
"""import random
num = random.randint(1,20)
flag = True
guess = 0
print("Guess my number 1-20")
while flag == True:

    guess = input()
    if not guess.isdigit():
        print("Invalid! enter only digits 1-20")
        break
    elif int(guess) < num:
        print("Too low , try again:")
    elif int(guess) > num:
        print("Too high, try again")
    else:
        print("Correct My number is %s"%(num))
        flag = False
"""
#divisibility checker
"""num = int(input("Enter an integer number:"))
if int(num / 5) and int(num / 6):
    print("%s is divisible by 5 and 6"%(num))
else:
    print("%s is not divisible by 5 and 6"%(num))"""

#divisibilty checker v2
"""num = int(input("Enter an integer number:"))
div1 = int(input("Enter first divisor:"))
div2 = int(input("Enter second divisor:"))
a = num // div1
b = num // div2
ar = num % div1
br = num % div2
r1 = False
r2 = False
if ar == 0 and br == 0:
    r1 = True
    r2 = True
elif ar == 0:
    r1 = True
elif br == 0:
    r2 = True
else:
    r1 = False
    r2 = False

if r1 and r2:
    print("%s is divisible by %s and %s.\nQuotients are %s and %s respectively "%(num,div1,div2,a,b))
elif r1:
    print("%s is divisble by %s.\nQuotient is %s"%(num,div1,a))
elif r2:
    print("%s is divisible by %s.\nQuotient is %s"%(num,div2,b))
else:
    print("%s is not divisble by %s or %s"%(num,div1,div2))
"""
#area of tri calculation via Heron's formula
"""from math import *
A = int(input("Enter length of side A:"))
B = int(input("Enter length of side B:"))
C = int(input("Enter lenght of side C:"))
s = (A+B+C)/2
x = s*(s-A)*(s-B)*(s-C)
area = sqrt(x)
print("Input lengths can form a triangle of area %.3f square units"%(area))"""

#some function thing 
"""def f(fx):
     print('fx =', fx, '/ id(fx) = ', id(fx))
     fx = 10
     print('fx =', fx, '/ id(fx) = ', id(fx))

x = 5
print('x =', x, '/ id(x) = ', id(x))
f(x)
print('x =', x, '/ id(x) = ', id(x))"""

#leap yr calculator
"""def leap(yr):
    c1 = yr % 4
    c2 = yr % 100
    c3 = yr % 400
    if not c1 and c2:
        print("%s is a leap year."%(yr))
        return
    elif not c1 and not c2 and not c3:
        print("%s is a leap year."%(yr))
        return
    else:
        print("%s is not a leap yr."%(yr))
    
yr = int(input("Please enter the year:"))
leap(yr)
"""
# activities based on outdoor temperature
"""temperature = int(input("Please enter the outdoor temperature:"))
if temperature <= -5:
    print("Go bowling")
elif -5<temperature<=0:
    print("Go skiing")
elif 0<temperature<= 20 :
    print("Go jogging")
elif 20<temperature<= 25:
    print("Play tennisl; wear white clothes")
elif 25<temperature<= 30:
    print("Go sun-tanning in the park")
else:
    print("Go swimming")"""

# calculating the cost of magical inked sheets
"""while True:
    number = int(input("Enter the number of magical inked sheets to print: "))
    if number > 0:
        print("Processing your request please wait...")
        if 0<number<=100:
            cost = 0.03 * number
            print("Cost of printing %s magical inked sheets is $%.2f"%(number,cost))
            break
        elif 100<number<300:
            remain = number - 100
            cost2 = remain * 0.02
            total = (100*0.03) + cost2
            print("Cost of printing %s magical inked sheets is $%.2f"%(number, total))
            break
        else:
            over = number - 100 - 200
            cost3 = over * 0.01
            total = (100*0.03) + (200*0.02) + cost3
            print("Cost of printing %s magical inked sheets is $%.2f"%(number,total))
            break
    else:
        print("Invalid number of sheets\nStart again.")"""

#Museum admission ticket calculator
"""def cost_calc(total_no_visitors, num_SCandPR):
    SCandPR_cost = num_SCandPR * 0
    num_others = total_no_visitors - num_SCandPR
    others_cost = num_others * 15
    total_cost = SCandPR_cost + others_cost
    print("The total cost of tickets:$%s\nThe cost of tickets for SC and PR:$%s\nThe cost of tickets of others:$%s"\
          %(total_cost, SCandPR_cost,others_cost))
    
total_no_visitors = int(input("Please enter the total number of visitors: "))
num_SCandPR = int(input("Please enter the number of SC and PR visitors: "))
cost_calc(total_no_visitors, num_SCandPR)"""

# average temperature reading for 1 day
"""temp_list = [20.5, 22, 21, 29.3, 28.2, 25, \
             26, 28, 26.3, 25.6, 29.3, 28.4, \
             24.5, 26.3, 25.5, 26.5, 23.3, 24.3, \
             25.4, 26.5, 23.3, 25.4, 26.3, 25.5]
total = 0
while len(temp_list)>0:  #while loop
    remove = temp_list.pop()
    total = total  + remove
    
average = total / 24
print("The average temperature for the day is: %.2f degree celsius."%(average))

total = 0   #for loop with range
for i in range(0, len(temp_list)):
    total = total + templist[i]

average = total/len(temp_list)
print(average)"""
#average temperature calculation using nested loops
"""list1 = [20,21,23,25,22]
list2 = [27,23,25,20,30,24]
list3 = [22,23,24,22]

all_rooms = [list1,list2,list3]
for room in all_rooms:
    total = 0
    for i in room:
        total = i + total
    average = total / len(room)
    print(total)
    print("Average temperature in room %s is %.1f"%(room,average))"""
    
    
#sqaure numbers generator 
"""multiplier = 0
multiplicand = 0
while product < 1000000:
    multiplier += 1
    multiplicand += 1
    product = multiplier * multiplicand
    print(product)"""
    
# multiplication table
"""multiplier = 5
multiplicand = 0
while multiplicand < 12:
    multiplicand += 1
    product = multiplier * multiplicand
    print("%s x %s = %s"%(multiplier,multiplicand,product))"""
#simple math calculator
"""check = True
while check == True:
    num1 = input("Enter first number/decimal(to quit enter any letter) : ")
    if num1.isalpha():
        print("Calculation program ended.")
        break
    else:
        num1 = float(num1)
    operator = str(input("Enter plus, minus, times or divide symbol: "))
    num2 = float(input("Enter second number/decimal: "))
    if operator == "+":
        total = num1 + num2
        print("%s + %s = %.3f"%(num1,num2,total))
    elif operator == "-":
        total = num1 - num2
        print("%s - %s = %.3f"%(num1,num2,total))
    elif operator == "x":
        total = num1 * num2
        print("%s x %s = %.3f"%(num1,num2,total))
    elif operator == "/":
        total = num1 / num2
        print("%s / %s = %s"%(num1,num2,total))
    else:
        print("Not programmed to handle that yet")
        check = int(input("To continue, enter 1\nTo end, enter 0: "))
        if check == 0:
            print("Calculation program ended.")
            check = False
        else:
            check = True """
#another version of a random number guessing game
"""print("Welcome to Number Guessing Game")
check = True
import random
tries = 1
tried = 4
num = random.randint(1,100)
while check == True :
    t1 = int(input("Try %s: Enter a number between 1 and 100(or -1 to end): "%(tries)))
    if tried == 0:
        print("Game over.\nCorrect number was %s"%(num))
        break
    if t1 == num:
        print("You've got it right, you're really lucky!")
        check = False
    elif t1 == -1:
        print("Guessing game ended.\nThe correct number was %s"%(num))
        check = False
    elif t1 < num:
        tries += 1 
        print("%s is lower than the correct number.%s tries left."%(t1,tried))
        tried -= 1 
    elif t1 > num:
        tries += 1
        print("%s is higher than the correct number.%s tries left"%(t1,tried))
        tried -= 1
    else:
        print("End of guessing game.n\Correct number was %s"%(num))
        break"""

# finding temperatures that exceed a certain value

"""temp_list = [20.1,24,27.3,30.1,26.4,22.2,20.1,24,\
             27.3,30.1,26.4,20.1,24,27.3,30.1,26.4,\
             20.1,24,27.3,30.1,26.4,20.1,24,27.3]
for temp in temp_list:                 # while loop 
    
    if temp > 25:
        print("Warning the temperature of %s°c has exceeded 25°c."%(temp))
        break
    else:
        print(str(temp)+"°c")

for temp in range(0,len(temp_list)):     #for loop with range
    if temp_list[temp] > 25:
        print("Warning the temperature of %s°c has exceeded 25°c."%(temp_list[temp]))
        break
    else:
        print(str(temp_list[temp])+"°c")"""
# finding average and highest temperature
"""temp_list = [20.1,24,27.3,30.1,26.4,22.2,20.1,24,\
             27.3,30.1,26.4,20.1,24,27.3,30.1,26.4,\
             20.1,24,27.3,30.1,26.4,20.1,24,27.3]
total = 0
for temp in temp_list:        #for loop with continue
    total = total + temp
    maximum =  max(temp_list)
    continue
average = total / len(temp_list)
print("The average reading of the day is {:.3f}°c, and the highest reading is {}°c."\
      .format(average,maximum))
total = 0
for temp in range(0,len(temp_list)):   #for loop with range and continue
    total = total + temp_list[temp]
    maximum = max(temp_list)
    continue
average = total/len(temp_list)
print("The average reading of the day is {:.3f}°c, and the highest reading is {}°c."\
      .format(average,maximum))"""
#battleship game (TO BE CONTINUED) 
"""def random_volley():
    list1 = ['A', 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' ,\
             'I' , 'J' , 'K' , 'L']
    import random
    volley = []
    for i in range(1,6):
        x = (random.choice(list1))
        y = random.randint(1,10)
        volley.append(str(x)+str(y))
        continue
    print(ships)
    return

list1 = ['A', 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' ,\
         'I' , 'J' , 'K' , 'L']
import random


ship_5 = []
y = random.randint(0,5)
x = (random.choice(list1))
for i in range(1,6):
    y+=1
    ship_5.append(str(x)+str(y))
    continue

    
while True:
    ship_4 = []
    y = random.randint(0,6)
    x = (random.choice(list1))
    for i in range(1,5):
        y+=1
        ship_4.append(str(x)+str(y))
    if any( x in ship_4 for x in ship_5):
        ship_4.clear()
    else:
        break
        
while True:   
    ship_3 = []
    y = random.randint(0,7)
    x = (random.choice(list1))
    for i in range(1,4):
        y+=1
        ship_3.append(str(x)+str(y))
    if any( x in ship_3 for x in ship_4):
        ship_3.clear()
    elif any(x in ship_3 for x in ship_5):
        ship_3.clear()
    else:
        break
    
while True:
    ship_2 = []
    y = random.randint(0,7)
    x = (random.choice(list1))
    for i in range(1,4):
        y+=1
        ship_2.append(str(x)+str(y))
        continue  
    if any(x in ship_2 for x in ship_3):
        ship_2.clear()
    elif any( x in ship_2 for x in ship_4):
        ship_2.clear()
    elif any( x in ship_2  for x in ship_5):
        ship_2.clear()
    else:
        break

while True:
    ship_1 = []
    y = random.randint(0,8)
    x = (random.choice(list1))
    for i in range(1,3):
        y+=1
        ship_1.append(str(x)+str(y))
        continue 
    if any(x in ship_1 for x in ship_2):
        ship_1.clear()
    elif any(x in ship_1 for x in ship_3):
        ship_1.clear()
    elif any(x in ship_1 for x in ship_4):
        ship_1.clear()
    elif any(x in ship_1 for x in ship_5):
        ship_1.clear()
    else:
        break

print(ship_1)
print(ship_2)
print(ship_3)
print(ship_4)
print(ship_5)
print("Welcome to battleship v1.0\nInstructions: You have 5 ships \n\
ship 1: 2 units\nships 2 and 3: 3 units each\nship 4: 4 units\nship 5: 5 units\n\
Objective: Destroy all of the opponent's ships\n")
print("You have 10 columns and 11 rows (lettered A to L)")"""

#nested loop activity number pattern
"""for i in range(1,4):
    for j in range(1,4):
        j*=i        
        print(j,end = '')
    print()"""

#nested loop activity, another number pattern
"""for i in range(1,6): #number of rows
    for j in range(1,6):
        if j <= 5 - i:
            print(".", end = "")
        else:
            print(i, end = "")
    print()"""

# calendar(30 days)
"""total = -7
print("{:<3s} {:<2s} {:<2s} {:<2s} {:<2s} {:<2s} {:<2s}".format(" S","M","T","W","Th","F","S"))
for i in range(1,7):
    for y in range(1,2):
        total +=7
        break
    for x in range(1,8):
            x+= total
            if x >= 31:
                break
            if 0<x<10:
                print(' '+str(x),end=' ')
            else:
                print(x,end=' ')
    print() """
#matrix addition
"""matrix1 = [[1.0, 2.0, 3.0],\
          [4.0, 5.0, 6.0],\
          [7.0, 8.0, 9.0]]

matrix2 = [[0.0, 2.0, 4.0],\
          [1.0, 4.5, 2.2],\
          [1.1, 4.3, 5.2]]
matrix3 = []
a = []
b = []
c = []

for i in range(3):
    for j in range(3):        
        x = matrix1[i][j] + matrix2[i][j]
        if i == 0:
            a.append(x)
        if i  == 1:
            b.append(x)
        if i == 2:
            c.append(x)
                
matrix3.append(a)
matrix3.append(b)
matrix3.append(c)
        
for z in matrix3:
    print(z) """

#system interface selection
"""options = ["reboot system now", "apply sdcard:update.zip",\
           "wipe data/ factory reset", "+++++Go Back+++++"]
x = 1
while True:
    print("Onix Recovery v2.5.1.0\n")
    for i in options:
            print(x,i)
            x+=1
            if x>4:
                x=1
    print("_______________________________")
    selected = int(input("Enter selection:"))
    if selected == 4:
        break
    print(options[selected-1])
    print() """
    
# Calculating total average
"""numbers = []
pos = 0
neg = 0
while True:
    num1 = float(input("Please enter a number or enter 0 to stop:"))
    if num1 == 0:
        break
    else:
        numbers.append(num1)
for i in numbers:
    if i > 0:
         pos += 1
    else:
        neg += 1
total = sum(numbers) 
average = total / len(numbers)
print("%s positive numbers have been read.\n%s negative numbers have been read.\n\
The sum of the non-zero numbers: %.2f\nThe average of the non-zero numbers:%.2f"
      %(pos,neg,total,average)) """

# Mastermind number guessing game (simplified)
"""import random
num = random.randint(100,999)
i = 0
while True:
    i += 1
    if i == 6:
        print("The correct number is {}".format(num))
        print("{:*^17}".format("End of game"))
        break
    print("Try #%s -"%(i),end = ' ')
    guess = int(input("Please enter your guess:"))
    if guess == num:
        print("{:^58}".format("Great! You have gotten the correct number!"))
        print("{:*^17}".format("End of game"))
        break
    else:
        print("{:^46}".format("#{} - Your guess is incorrect").format(i)) """
    
# mastermind guessing game (actual)      
"""import random
num = random.randint(100,999)
num_list = []
num_list[:0] = str(num)
guess_list = []
i = 0
wrong_position = 0
check = True
while check:
    i += 1
    if i == 11:
        print("The correct number is {}".format(num))
        break
    print("Try #%s -"%(i),end = ' ')
    guess = input("Please enter your guess(100-999):")
    guess_list[:0] = str(guess)
    wrong_position = 0
    correct = []
    right_position = 0
    for b in range(3):
       if guess_list[b] == num_list[b]:
           right_position += 1
           correct.append(b)
       elif guess_list[b] != num_list[b]:
           if guess_list[b] in num_list:
               y = guess_list[b]
               c = guess_list.count(y)
               d = num_list.count(y)
               if c <= d:
                   wrong_position += 1
               del c
               del d
    guess_list.clear()
    if right_position == 3:
         print("{:^58}".format("Great! You have gotten the correct number!"))
         print("{:*^17}".format("End of game"))
         check = False
    if check:
            print("        Try #{} - {} correct digit and position, \
{:.0f} correct digit but wrong position".format(i,right_position,wrong_position))"""


#balanced or unbalanced delimiters (parenthesis in this one)
"""x = str(input("Please enter your program in a string:"))
for a in x:
    count1 = x.count("(")
    count2 = x.count(")")
if count1 == count2:
    print("The program has balanced delimiters")
else:
    print("The program does not have balanced delimiters")"""

#prime number finders
"""while True:
    print("Enter a number or -1 to stop.")
    num = int(input("The program will find out the\
prime numbers less than or eqauls to it:"))
    if num == -1:
        break
    prime= "" 
    for x in range(1,num+1):
        a = 0
        for i in range(1,num+1):
            if not x%i:
                a += 1
        if a == 2:
            prime += str(x)
            prime += " "
            if a > 2:
                prime -= str(x)       
        del a            
    print(prime)"""
        
#mobile plans calculation
"""import math
data = int(input("Average monthly local data (GB) needed: "))
talk = int(input("Average monthly talk time (mins) needed: "))
print("{:10s} {:15s} {:15s} {:15s} {:15s} {:15s}"
      .format("Plan", "Phone Cost", "Monthly Cost", "Local Data(GB)",\
              "Talk time(mins)","Total Cost"))
plan = ["A","B","C","D","E"]
for a in range(5):
    for i in range(5):
        for letter in plan:
            if a == 0:
                if letter == "A":
                    excess_data = math.ceil(data - 0.1)
                    excess_talk = talk - 100
                    Plan,phone,month,local,t = ["A",1248,27.9,0.1,100]
            if a == 1:
                if letter == "B":
                    excess_data = data - 2
                    excess_talk = talk - 200
                    Plan,phone,month,local,t = ["B",1114,42.90,2,200]
            if a == 2:
                if letter == "C":
                    excess_data = data - 3
                    excess_talk = talk - 10000
                    Plan,phone,month,local,t = ["C",882,68.90,3,10000]
            if a == 3:
                if letter == "D":
                    excess_data = data - 6
                    excess_talk = talk - 10000
                    Plan,phone,month,local,t = ["D",641,95.90,6,10000]
            if a == 4:
                if letter == "E":
                    excess_data = data - 12
                    excess_talk = talk - 10000
                    Plan,phone,month,local,t = ["E",0,198.90,12,10000]
    if excess_data > 0:
        cost = excess_data * 10.70
        if cost > 188:
            cost = 188
    else:
        cost = 0
    if excess_talk > 0:
        cost_t = (excess_talk * 16.05)/100
    else:
        cost_t = 0
    total = phone + (month + cost + cost_t)*24
    print("{:10s} {:<15d} {:<15} {:<15} {:<15} ${:<15.2f}"
          .format(Plan,phone,month,local,t,total))"""

# find larger integer function
"""def find_larger(n1,n2):
    if n1 > n2:
          return n1  
    else:
        return n2    
            
n1 = int(input("Enter first integer: "))
n2 = int(input("Enter second integer: "))
print("The larger integer is {}".format(find_larger(n1,n2)))"""

#using above function to find largest of 4 integers
"""n1 = int(input("Enter integer: "))
n2 = int(input("Enter integer: "))
n3 = int(input("Enter integer: "))
n4 = int(input("Enter integer: "))
l1 = find_larger(n1,n2)
l2 = find_larger(n3,n4)
print("The largest integer is {}".format(find_larger(l1,l2)))"""

#even number checker
"""def is_even(n):
    if not n%2:
        return True
    else:
        return False

n = int(input("Enter number: "))
print(is_even(n))"""

#using above function to distinguish even from odd
"""num_list = [10, -13, 50, 5, 7, 24, 65, -40, 44, 30]
even = []
for i in num_list:
    if is_even(i):
        print(i,end=" ")"""
#related to function above

#power function
"""def power(x,n):
    import math
    print("The answer is",math.pow(x,n))
x = int(input("Enter base value: "))
n = int(input("Enter exponent value: "))
power(x,n)"""

#printing a sqaure 
"""def print_square(char,sides):
    for a in range(sides):
        for i in range(sides):
            print(char, end = ' ')
        print()

char = str(input("Enter character: "))
sides = int(input("Enter number: "))
print_square(char,sides)"""

#swapping values
"""num1 = 1
num2 = 2
x = num1
num1 = num2
num2 = x"""
#swapping values (shorter version)
"""num1 = 5
num2 = 3
num1, num2 = num2,num1"""

#list exercise
"""first_list = [ 1, 2, 3, 4, 5 ]
second_list = [ 2, 3, 4 ]
print(first_list[1:3])
print(first_list[:3])
print(first_list[3:])
print(first_list)
print(len(first_list))
print(min(first_list[1:3]))
print(first_list != second_list)
print(first_list[1:4] == second_list)
thirdList = first_list + second_list
print(thirdList)
print(4 in first_list)
print(4 not in second_list)
print(second_list in first_list)
print(second_list[1] in first_list[1:3])"""

# binary to decimal conversion
"""def binaryToDecimal(binary):
    b = list(binary)
    b.reverse()
    n = 0
    deci = []
    for i in b:
        currentDigit = int(i)
        deci.append(currentDigit * (2**n))
        total = sum(deci)
        n+=1
    return total
binary = input("Enter binary number: ")
total = binaryToDecimal(binary)
print("The decimal value is: ",total)""" 

#square_sum
"""def square_sum(numbers):
    num_list=[]
    total = 0
    for i in numbers:
        num = i**2 
        num_list.append(num)
    total = sum(num_list)
        
    print(total)
numbers = [1,2,2]
square_sum(numbers)"""

    

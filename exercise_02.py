Exercise 2: Write another program that prompts for a list of numbers
as above and at the end prints out both the maximum and minimum of
the numbers instead of the average

total = 0
average = 0

count = 0

input_num = []

while True:
    num = input("Please input a number:")

    if num == 'done':
        break
    else:
         try:
             num = float(num)
             input_num.append(num)
             
         except:
              
              print("Invalid input!")
              
for i in input_num:
     total = total + itervar
     count = count + 1

average = total/count

print(total,count,average)



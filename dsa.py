# numbers = list(map(int, input("Enter numbers : ").split()))

# if numbers:
#     largest = numbers[0]

#     for num in numbers:
#         if num > largest:
#             largest = num

#     print("The largest number is:", largest)
# else:
#     print("The list is empty.")



# num = list(map(int, input("enter numbers :").split()))

# if num:
#     addition = 0

#     for i in num:
#         if i >= 10:
#             addition = addition + i

#     print("sum :", addition)
# else:
#     print("empty")





# numbers = list(map(int, input("Enter numbers : ").split()))


# if numbers:
#     largest = numbers[0]
#     for num in numbers:
#         if num > largest:
#             largest = num

#     while largest in numbers:
            
#             numbers.remove(largest)

#             dublicate = numbers[0]

#             for num in numbers:
#                 if num == dublicate:
#                     numbers.remove(dublicate, num)

#             while second in numbers:
#                     second = numbers[0]
#                     if num > second:
#                          second = num
#     print("2nd  maximum :",numbers)
# else:
#     print("its empty")




# numbers = list(map(int, input("Enter numbers : ").split()))

# if len(numbers) < 2:
#     print("List must contain at least two numbers.")
# else:
#     largest = numbers[0]
#     for num in numbers:
#         if num > largest:
#             largest = num

#     while largest in numbers:
#         numbers.remove(largest)
#         print(numbers)
#         no_dupli = []
#         for x in numbers:
#             if numbers.count(x) == 1:
#                 no_dupli.append(x)
#                 print(no_dupli)

#                 if not numbers:
#                     print("There is no second maximum.")
#                 else:
#                     second = no_dupli[0]
#                     for num in no_dupli:
#                         if num > second:
#                             second = num
#     print("2nd maximum :", second)







# 2nd of 14/ 08/ 2026


# timings = list(map(int, input("Enter numbers : ").split()))

# current = 0
# longest = 0 
# for time in timings:
#     if time <200:
#         current += 1
#         longest=max(current,longest)
#     else:
#         current=0
# print(longest)



# 3rd 14/08/26

# n = int(input("no of employees :"))
# count = 0
# maximum = 0

# for i in range(n):
    
#     attendance = list(map(int, input("enter in 0 or 1 :")))
#     for a in attendance:
#         if a == 0:
#             count += 1
#             if count > max:
#                 maximum = count
# print("employee :", i )
# print("with absent days :", maximum)




# numbers = list(map(int, input("Enter numbers : ").split()))

# if not numbers:
#     print("its empty")
# else:
#     largest = numbers[0]
#     for num in numbers:
#         if num > largest:
#             largest = num

#     while largest in numbers:
#         numbers.remove(largest)

#     if not numbers:
#         print("There is no 2nd maximum.")
#     else:
#         second = numbers[0]
#         for num in numbers:
#             if num > second:
#                 second = num

#         while second in numbers:
#             numbers.remove(second)

#         print("2nd maximum (unique) :", second)




# 18 / 08 / 26 

# t = int(input(""))

# for _ in range(t):
#     A, WD= map(int, input("").split())
#     G = input("gender :")
#     if A >= 18 and A <= 40:
#         if G == "femail":
#             wages = (750 * WD)
#         else:
#             wages = (700 * WD)
#         print(wages)
#     else:
#         print("invalid age ")


        

    

# t = int(input("Enter total number of workers: ")) 

# for worker in range(1, t + 1): 
#     print("worker :",worker) 
    
#     age = int(input("Age: ")) 
#     working_days = int(input("Working Days: ")) 
#     gender = input("Gender (male/female): ").strip().lower() 
    
#     if 18 <= age <= 40: 
#         if gender == "female": 
#             wages = 750 * working_days
#         else: 
#             wages = 700 * working_days
#         print("Worker wages:", wages)
#     else: 
#         print("Invalid age")



# t = int(input("no. of department :"))

# for department in range(1, t + 1):
#     print("department :",department)

#     n = int(input("no of workers in department :"))

#     for worker in range(1, n + 1):
#         print("worker :", worker)

#         age = int(input("Age :"))
#         working_days = int(input("Working Days: ")) 
#         gender = input("Gender (male/female): ").strip().lower()

#         if 18 <= age <= 40: 
#             if gender == "female": 
#                 wages = 750 * working_days
#             else: 
#                 wages = 700 * working_days
#             print("Worker wages:", wages)
#         else: 
#             print("Invalid age")


# 13 / 08/ 26

# n = int(input("neter no. :"))
# square = n * n
# print("square :",square)


# n = int(input("enter :"))

# for i in range(1, n + 1):
#     if i * i == n:
#         print(i)
#         break
#     else:
#         print("invalid square")


# n = int(input("enter the range :"))
# sum = 0
# num = []

# for i in range(n):
#     num.append(int(input("enter the numbers :")))

#     for i in range(n):
#         square = i * i
#         sum = sum + square
    
# print(sum)



# a = int(input("range :"))

# num = []
# perfect_square = []

# for n in range(a):
#     num.append(int(input("enter the number :")))
#     for i in range(1, n + 1):
#         if i * i == n:
#             perfect_square.append(n)
#     print(max(perfect_square))
    

# a = int(input("range :"))

# num = []
# perfect_square = []

# for n in range(a):
#     numbers = int(input("enter the number :"))
#     num.append(numbers)
    
#     for i in range(1, numbers + 1):
#         if i * i == numbers:
#             perfect_square.append(numbers)
#             break 

# print(max(perfect_square))









# 19 aug 2026 



# t = int(input("no. of branches :"))

# for branches in range(1, t + 1):
#     print("department :",branches)

#     n = int(input("no of department :"))

#     for dept in range(1, n + 1):
#         print("dept :", dept)

#         m = int(input("no of workers in dept :"))

#         for workers in range(1, m + 1):
#             print("worker :", workers)

#             age = int(input("Age :"))
#             working_days = int(input("Working Days: ")) 
#             gender = input("Gender (male/female): ").strip().lower()

#             if 18 <= age <= 40: 
#                 if gender == "female": 
#                     wages = 750 * working_days
#                 else: 
#                     wages = 700 * working_days
#                     print("Worker wages:", wages)
#             else: 
#                 print("Invalid age")








# workers = int(input("Enter number of workers: "))

# ages = []
# genders = []
# days = []

# for i in range(workers):
#     ages.append(int(input("Age: ")))
#     genders.append(input("Gender (M/F): ").upper())
#     days.append(int(input("Working days: ")))

# for i in range(workers):

#     if 18 <= ages[i] <= 40:

#         if genders[i] == "F":
#             wages = 750 * days[i]
#         else:
#             wages = 700 * days[i]

#         print("Worker", i + 1, "wages =", wages)

#     else:
#         print("Worker", i + 1, "Invalid age")




# t = int(input("no. of department :"))

# for department in range(1, t + 1):
#     print("department :",department)

#     n = int(input("no of workers in department :"))

#     for worker in range(1, n + 1):
#         print("worker :", worker)

#         age = int(input("Age :"))
#         working_days = int(input("Working Days: ")) 
#         gender = input("Gender (M/F): ").strip().upper()

#         if 18 <= age <= 40: 
#             if gender == "F": 
#                 wages = 750 * working_days
#             else: 
#                 wages = 700 * working_days
#             print("Worker wages:", wages)
#         else: 
#             print("Enter apperopriate age")



# T = int(input())

# for _ in range(T):
#     N = int(input())
#     A = list(map(int, input().split()))

#     odd = 0
#     even = 0

#     for num in A:
#         if num % 2 == 0:
#             even += 1
#         else:
#             odd += 1

#     if odd == even:
#         print(N)
#     else:
#         print(2 * min(odd, even) + 1)



# 20 / 8/ 26

# H = int(input())
# CC = float(input())
# S = int(input())

# if H > 50 and CC > 0.7 and S > 560:
#     print("Grade : 10")
# elif H > 50 and CC > 0.7 and S <= 560:  
#     print("Grade : 9")
# elif CC > 0.7 and S > 560 and H <= 50:  
#     print("Grade : 8")
# elif H > 50 and S > 50 and CC < 0.7:
#     print("Grade : 7")
# else:
#     print("Grade : 0")



# t = int(input("no of samplers :"))

# for sample in range(1, t + 1):
#     print("sample :", sample)
#     H = int(input())
#     CC = float(input())
#     S = int(input())
#     if H > 50 and CC > 0.7 and S > 560:
#         print("Grade : 10")
#     elif H > 50 and CC > 0.7 and S <= 560:  
#         print("Grade : 9")
#     elif CC > 0.7 and S > 560 and H <= 50:  
#         print("Grade : 8")
#     elif H > 50 and S > 50 and CC < 0.7:
#         print("Grade : 7")
#     else:
#         print("Grade : 0")


# n = int(input("no. of production lines :"))

# for line in range(1, n + 1):
#      print("line :", line)

#      t = int(input("no of sample :"))

#      for sample in range(1, t + 1):
#         print("sample :", sample)
#         H = int(input())
#         CC = float(input())
#         S = int(input())
#         if H > 50 and CC > 0.7 and S > 560:
#             print("Grade : 10")
#         elif H > 50 and CC > 0.7 and S <= 560:  
#             print("Grade : 9")
#         elif CC > 0.7 and S > 560 and H <= 50:  
#             print("Grade : 8")
#         elif H > 50 and S > 560 and CC < 0.7:
#             print("Grade : 7")
#         else:
#             print("Grade : 0")
         


# 14/08/26

# n = int(input("no of empyoyee :"))

# attendance = []
# count = 0
# counter = []

# for emp in range(1, n + 1):
#     print("employee", emp)

#     A = list(map(int, input("atten :").split()))
#     attendance.append(A)

#     for i in range(attendance):
#         if i == 1:
#             count += 1
            

# 21 / 08/26


# n = int(input())

# for i in range(n):
#     t = n * "*"
#     a = int(input())

#     for j in range(a):
#         print(t)




# n = int(input())
# for i in range(n):
#     m = int(input())
#     for j in range(1, m + 1):
#         print(j * "*")


# n = int(input())

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()


# 22/8/26


# t = int(input())

# B = []
# Maxi = 0

# for i in range(t):
#     ID = int(input("id :"))
#     Name = input("name :")
#     balance = int(input("balance :"))
#     B.append({ "balance": balance, "name": Name})
# for M in B:
#     if M > Maxi:
#         Maxi = M
# print("max-balance : ", Maxi)











# users = []

# n = int(input("Enter number of users: "))

# for i in range(1,n+1):
#     print("user :", i)
#     userId = int(input("Enter user id: "))
#     name = input("Enter name: ")

#     users.append({"id": userId,"name": name})
#     orders = []
#     m = int(input("Enter number of orders: "))
#     for j in range(m):
#         print("order :", j)
#         userId = int(input("Enter userId: "))
#         product = input("Enter product: ")
#         orders.append({"userId": userId,"product": product})
#         result = []
#         for order in orders:
#             for user in users:
#                 if order["userId"] == user["id"]:
#                     result.append({"name": user["name"],"product": order["product"]})
#     print("\n Merged Data:")
#     for item in result:
#         print(item)





# t = list(map(int, input().split())) 

# missing = []
# new_arr = []

# n = int(input()) 

# for j in range(1, n + 1):
#     missing.append(j)

# for a in missing:
#     if a not in t:  
#         new_arr.append(a)

# print(new_arr)




# 24 / 08 / 26


# n = int(input())
# user_names = []
# for i in range(n):
#     name = input("enter name :")
#     user_names.append(name)

# longest = user_names[0]        


# for name in user_names:
#     if len(name) > len(longest):
#         longest = name

# print("longest :", longest)



# age = int(input("age :"))
# is_weekend = input("True/False :")
# has_student_card = input("True/False :")

# if age < 5:
#     price = "free"
# elif age >= 5 and age <= 11:
#     price = 150
# elif age >= 60 :
#     price = 100
# else:
#     price = 250
#     if is_weekend == True:
#         price = price + 50
#         if age > 11 and age < 60  and has_student_card == True:
#             price = price - 50
# print("price :", price)



# n = input("enter the word :")

# for i in n:
#     if n[i] == 










# 25/8/26



# n = int(input("Number of files: "))

# count_pdf = 0
# count_jpg = 0
# count_png = 0

# for _ in range(n):
#     file = input("File name: ")

#     if ".pdf" in file:
#         count_pdf += 1
#     elif ".jpg" in file:
#         count_jpg += 1
#     elif ".png" in file:
#         count_png += 1

# output = {
#     "pdf": count_pdf,
#     "jpg": count_jpg,
#     "png": count_png
# }

# print(output)




# name = input("Enter username: ")

# reverse = ""

# for i in range(len(name) - 1, -1, -1):
#     reverse += name[i]

# print(reverse)




# word = (input("enter a word :"))

# print(word.capitalize())





# t = int(input("range :"))
# count = 0


# for _ in range(t):
#     num = list(map(int, input("enter num :").split()))

#     for i in range(num):
#         for j in range(num + 1, num):
#             if i == j :
#                 count += 1
#                 num.remove(j)
#     print(i, count)




# numbers = list(map(int, input("Enter numbers: ").split()))

# count = 0

# for i in range(len(numbers)):

#     if numbers[i] != -1:
#         count = 1

#         for j in range(i + 1, len(numbers)):

#             if numbers[i] == numbers[j]:
#                 count += 1
#                 numbers[j] = -1

#         print(numbers[i], ":", count)



# k = int(input())

# numb = list(map(int, input("enter numbers :").split()))
# for i in range(len(numb)):
#     if numb[i] != -1:
#         for j in range(i + 1, len(numb)):

#             if numb[i] + numb[j] == k:
#                 print(numb[i], numb[j])


# k = int(input("value of K :"))

# num = list(map(int, input("enter numbers :").split()))
# count = 0
# longest = []
# for i in range(len(num)):
#     if num[i] != -1:
#         for j in range(i + 1, len(num)):
#             if num[i] + num[j] == k:
#                 count += 1
#         else:
#             print("output :", 0)     
#     print("output :", count)



# 3/09/2007

# t = int(input("range :"))
# req = []
# for i in range(t):
#     ids = int(input("id :"))
#     status = input("sucess/failed :")

#     if status == "failed":
#         req.append({"id": ids, "status": status})
# print(req)
    



# notification = input("notification :").split()
# result = {}
# for n in notification:
#     diff = n.split(".")[1]
#     if diff in result:
#         result[diff] += 1
#     else:
#         result[diff] = 1
# print(result)



# 7/9/26

# n = int(input())

# for i in range(n, 0, -1):
#     print("*"*i) 
   

        
# n = int(input())

# for i in range(n, -1, -1):
#     a = n-i
#     print(" "*i, "*"*a)



# r = int(input())

# for i in range(r, 0, -1):
#     if i == 1 or i == r:
#         print("*"*r)
#     else:
#         print("*"+" "*(r-2) + "*")



# 08/09/26


# t = int(input("range:"))

# all_f = []
# Max = 0


# for i in range(t):
#     fruits = input("fruit :")
#     price = int(input("price :"))

#     all_f.append({"fruits": fruits, "price": price})
#     if price >= Max:
#         Max = price
#         fmax = fruits

# print("max:", fmax)
# print(all_f)




# num = list(map(int, input("enter numbers :").split()))

# maximum = num[0]
# minimum = num[0]

# for i in range(len(num)):
#     if num[i] < minimum:
#         minimum = num[i]
        
#     if num[i] > maximum:
#         maximum = num[i]

# print("max :", maximum)
# print("min :", minimum)



# num = list(map(int, input("enter numbers :").split()))

# dupli = 0
# count = []

# k = int(input())
# for i in num:
#     for j in num:
#         if i == j:
#             dupli = i
#             for l in range(num, dupli, j):
#                 count.append(l)       
# print(len(count))


# 11/09/26

# n = input("enter text :")

# count = 0
# letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

# for i in n:
#     for l in letters:
#         if i == l:
#             count += 1
# print(count)



# n = list(map(str, input("enter text:").split()))

# count = 0
# vovel = "aeiouAEIOU"

# for i in n:
#     for j in vovel:
#         if i[0] == j:
#             count += 1
# print(count)



# n = int(input())

# for i in range(n, -1, -1):
#     a = ((n-i)*2) - 1
#     print(" "*i, "*"*a)

# for j in range(n):
#     b = (n-1) - j
#     c = n - b
#     d = (b*2)-1
#     print(" "*c, "*"*d)




# days = int(input("Enter number of days: "))
# charge = 0

# if days <= 5:
#     charge = days * 2
# elif days <= 10:
#     charge = (5 * 2) + (days - 5) * 3
# elif days <= 15:
#     charge = (5 * 2) + (5 * 3) + (days - 10) * 4
# else:
#     charge = (5 * 2) + (5 * 3) + (5 * 4) + (days - 15) * 5

# print(charge)





n = int(input("Enter range: "))
D = []

for _ in range(n):
    days = list(map(int, input("Enter the particular days: ").split()))
    
    for day in days:
        charge = 0
        if day <= 5:
            charge = day * 2
        elif day <= 10:
            charge = (5 * 2) + (day - 5) * 3
        elif day <= 15:
            charge = (5 * 2) + (5 * 3) + (day - 10) * 4
        else:
            charge = (5 * 2) + (5 * 3) + (5 * 4) + (day - 15) * 5
            
        D.append(charge)

print(D)



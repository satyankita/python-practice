# lecture 1 


# print("Hello Satya 🚀", "how are you")
# print("Hello, World!")
# print(98)
# print(2+6)

# name = "satya"
# age = 18
# price = 22.78
# a = None
# old = True

# print(name)
# print("my age is = ", age)
# print(type(name))
# print(type(age))
# print(type(price))
# print(type(a))
# print(type(old))

# a1 = 7
# a2 = 4
# sum = a1 + a2
# print(sum)
# print(a1 - a2)
# print(a1 * a2)
# print(a1 / a2 )
# print(a1 % a2)
# print(a1 ** a2)
# print( a1 == a2)
# print( a1 != a2)
# print( a1 >= a2)
# print( a1 <= a2)
# print( a1 < a2)
# print( a1 > a2)

# num = 10 
# num += 10
# print("num :", num)

# print (not False)

# b1 = 24
# b2 = 55
# print(not (b1 > b2))
# print((b1 == b2)and (b1 <b2))

# b3 = True
# b4 = False
# print(b3 and b4)
# print(b3 or b4)

# type conversion
# automatoc

# x = 2
# y = 4.25

# sum = x + y
# print(sum)

# #casting 

# x1 = int("2")
# y1 = 6.98

# print(type(x1))
# print(x1 + y1)



# valu = input("b Enter a value ")
# print(type(valu), valu)

# # practice questions

# n1 = int(input("enter n1:")) 
# n2 = int(input("enter n2:"))
# print( "sum = ",n1 + n2)

# length = int(input("enter l:")) 
# breath = int(input("enter b:"))
# print( "side = ",(length + breath)* 2)

# aa = float(input("enter first :"))
# bb = float(input("enter second :"))

# print("avg =", (aa+bb)/2)

# aaa = int(input("first:"))
# bbb = int(input("second:"))

# print(aaa >= bbb)


# a = int(input())

# if a % 2 == 0:
#     print("even")
# else:
#     print("odd")

# x = input().strip()


# if x[0] != x[1]:
#     print("YES")
# else:
#     print("NO")


# b = input().strip()

# num = 0

# number = abs(int(b))

# while number > 0:
#     digit = number % 10

#     digitsum += digit
#     number = number // 10
# print(digitsum)


# def sum_of_digits(n):
#     total_sum = 0
    
#     n = abs(n)
    
#     while n > 0:
#         digit = n % 10       
#         total_sum += digit   
#         n = n // 10          
        
#     return total_sum

# number = int(input("Enter an integer: "))
# print("Sum of digits:", sum_of_digits(number))


# n = int(input())

# for i in range(n):
#     count = 0
#     if n % i == 0:
#         count += 1
#         if count == 2:
#             print("yes")
#     else:
#         print("no")

# num = int(input("Enter an integer: "))
# is_prime = num > 1  
# for i in range(2, num):
#     if num % i == 0:
#         is_prime = False
#         break 

# print("Prime" if is_prime else "Not Prime")



# n = int(input())
# for i in range(n):
#     runs = list(map(int, input("enter the scores").split(' ')))
#     count = 0
#     for score in runs:
#         if score >= 40:
#             print("quilified")
#             count += 1
#         else:
#             print("not quilifies")
# print(count)


# n = int(input())

# for i in range(1, n + 1):
#     count = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             count += 1
            
#     if count == 2:
#         print(f"{i} is prime")
#     else:
#         print(f"{i} is not a prime")



#7TH APRIL



# MRP, discount = map(int, input().split())

# if discount >= 0 and discount <= 100:
#     sp = (MRP // 100) * discount
#     print(MRP - sp)
# else:
#     print("invalid discount")



# t = int(input())

# for _ in range(t):
#     n = int(input())
    
#     MRP = list(map(int, input().split()))
    
#     discount = list(map(int, input().split()))
    
#     for mrp, discount in zip(MRP, discount):
#         sp = mrp - (mrp * discount) / 100
#         print(sp)


# t = int(input())
# for category in range(1,t + 1):
#     print("category :", category)
#     n = int(input())
#     MRP = [int(x) for x in input("mrp :").split()]
#     discount = [int(x) for x in input("dis :").split()]

#     for i in range(n):
#         mrp = MRP[i]
#         dis = discount[i]

#         sp = mrp - (mrp * discount) / 100

#         print(sp)




# t = int(input())

# for category in range(1, t + 1):
#     print("Category :",category)
    
#     n = int(input())
    
#     mrp_list = [int(x) for x in input().split()]
#     discount_list = [int(x) for x in input().split()]
    
#     for i in range(n):
#         mrp = mrp_list[i]          
#         discount = discount_list[i] 
        
#         sp = mrp - (mrp * discount) / 100
        
#         print("Product", i + 1, ": SP =", sp)

        



# 8 aug 

# t = int(input("no. of tasks :"))

# for _ in range(t):
#     n = list(map(int, input("enter task compleated :").split()))
#     count = 0
#     if n >= 50 and n % 2 == 0 :
#         count += 1
#         print("employee no. :",count )
# print(count)






# t = int(input("no. of tasks: "))

# count = 0
# new = []

# for _ in range(t):
#     tasks_list = [int(x) for x in input("tasks: ").split()]

#     for n in tasks_list:
#         if n >= 50 and n % 2 == 0:
#             count += 1
#             new.append(n)
#             print("Employee qualified with tasks:", n)

# print("Total qualified employees:", count)
# print("Qualified tasks:", new)

# if len(new) >= 2:
#     max1 = max(new)
#     new.remove(max1)
#     max2 = max(new)

#     print("max 1 =", max1)
#     print("max 2 =", max2)

# elif len(new) == 1:
#     print("max 1 =", new[0])
#     print("No second maximum")

# else:
#     print("No qualified employees")
# percentage = (max1 * 90) // 100

# print("90% =", percentage)

# for i in new:
#     if i >= percentage:
#         print("Promoted employee:", i)




# t = int(input("no of products :"))
# for _ in range(t):
#     products = [int(x) for x in input("product :").split()]
#     discount = [int(x) for x in  input("discount :").split()]

#     for i in range(len(products)):
#         sp = (products // 100) * discount 

#     print(sp) 





# t = int(input("no of products :"))

# bill = []

# for _ in range(t):
#     products = [int(x) for x in input("product :").split()]
#     discount = [int(x) for x in input("discount :").split()]

#     for i in range(len(products)):
#         if 0 <= discount[i] <= 100:
#             sp = products[i] - (products[i] * discount[i]) / 100
#             bill.append(sp)
#             print("Selling price for item:", sp)
#         else:
#             print("invalid discount")

# print("All Selling Prices in Bill:", bill)



#11 aug


# t = int(input("range :"))
# for _ in range(t):

#     sp = [int(x) for x in input("Sp :").split()]
#     cp = [int(x) for x in input("Cp :").split()]

#     profit = sp - cp

#     for i in range(len(cp)):
#         if sp >= cp:
#             print("profit :",profit)
#         else:
#             print("invalid")


# t = int(input("range :"))

# for category in range(1, t + 1 ):
#     print("Category :",category)

#     n = int(input("no of products :"))

#     sp_list = [int(x) for x in input("Sp :").split()]
#     cp_list = [int(x) for x in input("Cp :").split()]

#     for i in range(n):
#         sp = sp_list[i]
#         cp = cp_list[i]
        
#         profit = sp - cp

#         if sp >= cp:
#             print("Profit for item :", profit)
#         else:
#             print("Invalid for item")




# t = int(input("no. of category :"))

# for category in range(1, t + 1):
#     print("--- Category", category, "---")

#     n = int(input("no of products in category :"))

#     sp_list = [int(x) for x in input("sp :").split()]
#     cp_list = [int(x) for x in input("cp :").split()]

#     category_profit = 0

#     for i in range(n):
#         sp = sp_list[i]
#         cp = cp_list[i]
        
#         profit = sp - cp

#         if sp >= cp:
#             print(f"Product {i + 1} Profit:", profit)
#             category_profit += profit
#         else:
#             print(f"Product {i + 1}: Loss / Invalid")

#     print("Total Profit for this Category:", category_profit)
#     print()



# t = int(input("rage of list : "))

# for _ in range(t):
#     a = list(map (input("fail / sucess :").split()))
    
#     count = 0
#     for i in range(a):
#         if i == "fail":
#             count += 0
#             if count == 3 :
#                 print("locked", i)
#                 break
#         else:
#             count = 0
#     print("account safe")



# a = input().split()
# count = 0

# for status in range(len(a)):
#     if a[status] == "fail":
#         count += 1
#         if count == 3:
#             print("Locked", status)
#             break
        
#     else:
#         count = 0
#         print(" Account safe")


# raw_input = input("Enter server response times: ")

# cleaned_data = raw_input.replace("[", "").replace("]", "").split(",")
# readings = []
# for item in cleaned_data:
#     if item.strip():  
#         readings.append(int(item.strip()))

# max_streak = 0
# current_streak = 0

# for time in readings:
#     if time < 200:
#         current_streak += 1
#         if current_streak > max_streak:
#             max_streak = current_streak
#     else:
#         current_streak = 0

# print(f"Longest healthy streak = {max_streak}")







# readings = [int(x) for x in input("Enter response times: ").split()]

# max_streak = 0
# current_streak = 0

# for time in readings:
#     if time < 200:
#         current_streak += 1
#         if current_streak > max_streak:
#             max_streak = current_streak
#     else:
#         current_streak = 0

# print("Longest healthy streak =", max_streak)








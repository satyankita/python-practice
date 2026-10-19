
    # dictionary 

# info = {
#     "name" : "my name",
#     "sub" : ["aaa", "bbb", "cdefd"],
#     "age": 18,
#     12.8 : 98.8
# }

# print(inf)


# arr = [1, 2, 3, 4, 5, 6]

# def factorial(arr):
#     sum = 0
#     for i in arr:
#         sum+=1
#     return sum
# arr = [1, 2, 3, 4, 5]
# print(sum(arr))    




# def factorial(n):
#     if n==1:
#         return 1
#     return n* factorial(n-1)
# print(factorial(5))


# def sum_digits(n):
#     if n == 0:
#         return 0

#     return n % 10 + sum_digits(n // 10)

# print(sum_digits(1234))


# def sumOf(arr):
#     sum = 0
#     for i in arr:
#         sum += i 
#         return sum 
# arr = [1, 4, 7,8, 7]
# print(sum(arr))


# def sum1(a):
#     sum == 0
#     for i in a:
#         sum += i
#         return sum 
# a = [1, 2, 9, 6,]
# print(sum(a))





# def sum2(b):
#     sum = 1

#     for i in b:
#         sum *= i

#     return sum

# b = [1, 2, 9, 6]
# print(sum2(b))

# def sum3(c):
#     sum = 1

#     for i in c:
#         sum *= i
#         return sum

# c = [4, 5, 6, 7, 8]
# print(sum3(c))


# def SumUp(num):
#     sum = 0
#     for a in num:
#         sum += a
#         return sum
# num = [3, 5, 9, 2, 9]
# print(sum(num))





# def table(n, i=1):
#     if i > 10:
#         return

#     print(n * i)
#     table(n, i + 1)

# table(5)   # Change 7 to any number


# n = 5
# sum = 0

# for i in range(1, n+1):
#     sum += i

# print(sum)


for i in range(4):
    for j in range(4):
        print("*", end="")
    print()

s = "banana"

count = 0

for ch in s:
    if ch in "aeiou":
        count += 1
print(count)

print(s[::-1])


if s == s[:: -1]:
    print("palindrome")
else:
    print("not palindrome")



arry = [19, 77, 6, 45]
print(max(arry))


max_num = arry[0]
sec = arry[0]
for i in arry:
    if i > max_num:
        sec = max_num
        max_num = i
    elif i > sec:
        sec = i

print("Maximum =", sec)

# min_num = arry[0]
# for i in arry:
#     if i < min_num:
#         min_num = i
# print("minimum:", min_num)





# n = int(input("how many elements :"))

# arr = []

# for i in range(n):
#     num = int(input())
#     arr.append(num)

# max = arr[0]
# for i in arr:
#     if i > max:
#         max = i

# print("max:", max)


students = {
    "name": "sattya",
    "age": 48,
    "contacr": {
        "mail": "asdfghj",
        "phone": 3456789
    }
    
}



print(students["contacr"]["mail"])

students["city"] = "delhi"
print(students)



# string =  "PytHOn"

# upp = 0
# low = 0

# for ch in string:
#     if ch.isupper():
#         upp += 1
#     else: 
#         low += 1
# print("upp: ", upp, "low: ", low)


# for ch in string:
#     print(ch, "=", string.count(ch))


# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()
# str1 = "this is first line .\n here is second"
# len1 = len(str1)

# print(str1)
# print(len(str1))

# str2 = 'this'
# str3 = """this"""
# print(str2+str3)
# ch = str3[0]
# print(ch)
# print(str3.capitalize())

# str4 = "Apna college"
# print(str4[1:4])
# print(str4[-8:-2])
# print(str4.endswith("ege"))
# print(str4.replace("college", "mera"))
# print(str4.replace("a", "e"))
# print(str4.find("o"))
# print(str4.count("e"))

# N1 = input("enter your name:")
# length1 = len(N1)
# print("length ",length1)

# N2 = "hi , do$ you know $$ this sign"
# print(N2.count("$"))


age1 = 20

if (age1 >= 18):
    print("can vote & apply for licence")
else:
    print("cant drive")

light = "blue"

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("wait")
else:
    print("none")


# marks = int(input("enter your marks : "))

# if(marks >= 90):
#     print("A")
# elif((marks < 90) and (marks >= 80)):
#     print("B")
# elif((marks < 80) and (marks >= 70)):
#     print("C")
# elif(marks < 70):
#     print("D")

age2 = 34

# nesting
if(age2 >= 18):
    if(age2 >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")


# practice question

# numb = int(input("enter any number : "))

# if (numb % 2 == 0):
#     print("even")
# else:
#     print("odd")

# if (numb % 7 == 0):
#     print("multiple of 7")
# else:
#     print("not the multiple of 7")


# gratest number from three 

p = 8
q = 5
r = 7
s = 9

if (p >= q and p >= r and p >= s):
    print("max1 =", p)
elif (q >= r and q >= s):
    print("max =", q)
elif (r >= s):
    print("max =", r)
else: 
    print("max =", s)


    # lecture 3 

    # list = [2, 1, 3, 5, 4]
    # list = [ "apple", "banana", "mango", "chiku"]
    # list.append(6)
    # list.append("grapes")
    # print(list)

    # print(list.sort())
    # print(list)

    # print(list.sort(reverse=True))
    # print(list)

    # print(list.reverse())
    # print(list)

    # list.insert(1, 7)
    # print(list)

    # list.remove(7)
    # print(list)

    # list.pop(3)
    # print(list)

    # tuples

    # tup = (2, 4, 5, 8, )
    # print(type(tup))
    # print(tup[0])
    # print(tup.count(2))
    # print(tup.index(8))

    # practice questions 
# movies = []
# mov = input("enter your 1st fev movie :")
# movies.append(mov)
# mov = input("enter your 2nd fev movie :")
# movies.append(mov)
# mov = input("enter your 3rd fev movie :")
# movies.append(mov)

# print(movies)

# movie1 = input("enter your 1st fev movie :")
# movie2 = input("enter your 2nd fev movie :")
# movie3 = input("enter your 3rd fev movie :")

# list = [ movie1, movie2, movie3]
# print(list)


# palindrome 
# pal = [1, 2, 3, 2, 1]
# pal2 = [1, 2, 3, 4]

# copy_pal = pal2.copy()
# copy_pal.reverse()
# if(copy_pal == pal2):
#     print("palindrome")
# else:
#     print("not a pelindrome")


# tup = ("A", "B", "A", "A", "C", "B", "F")
# print(tup.count("A"))

# grade = ["A", "B", "A", "A", "C", "B", "D"]
# grade.sort()
# print(grade)


# Write a program to calculate the sum of numbers from 1 to N using a while loop.

# number = int(input("enter starting of num :"))
# N = int(input("enter ending num :"))
# i = number
# if(i <= N, i++):


mov = []
print(mov.append("abc"));
print(mov.append("cba"));
print(mov.append("bac"));
print(mov)

pel1 = [1,2,3];


copy1 = pel1.copy()
copy1.reverse()


if (pel1 == copy1):
    print("yes")
else:
    print("no")



mar = ["A", "C", "B", "B", "A", "B", "C", "D","A",]

# print(mar.count("D"))
mar.sort()
print(mar)



    


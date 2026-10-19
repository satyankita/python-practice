# print("hello")

# def avg(a = 1, b= 1, c = 1):
#     three_avg = a+b+c 
#     sumr = three_avg / 3

#     print(sumr)

# avg(4, 3, 2)
    

# def space():
#     list =[4, 5, 6, 2, 4]

#     print(len(list))

#     for i in list:
#         print(i, end="\n")

    
#     print(list[3])
# space()


# def fec(n):
#     fact = 1

#     for i in range(1, n+1):
#         fact *= i
#     print(fact)


# fec(7)


# def ind_ru(x):
#     usd = 83*x
#     print(usd)

# ind_ru(10)


# def oddif():
#     num = int(input("enter a number: "))
#     if num % 2 == 0:
#         print("even")
#     else:
#         print("odd")

# oddif()


def show(n):
    if (n == 0):
        return 
    
    show(n - 1)
    print(n)

show(5)

def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)
    
print(fact(4))

def sumof(n):
    if (n == 0):
        return 0
    return n + sumof(n-1)
    
print(sumof(5))



def alllist(li, idx=0):

    
    if (idx == len(li)):
        return
    print(li[idx])
    alllist(li, idx + 1)
lis = [3, 4, 6, 2, 4]
    
alllist(lis)

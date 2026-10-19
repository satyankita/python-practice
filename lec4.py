# info = {
#     "key" : "value",
#     "name" : "satya",
#     "learning": "coding",
#     "age": "18",
#     "is_adult": True,
#     "marks": 85.8,
#     "subjects" : {
#         "phy" : 88,
#         "che" : 45,
#         "math" :56
#     }
# }
# print(info["name"])
# print(info["age"])

# info["name"] = "satyankita"
# print(info)

# info["surname"] = "singh"
# print(info)

# print(info.keys())
# print(list(info.keys()))
# print(len(info))
# print(len(info.keys()))
# print(list(info.values()))
# print(list (info.items()))
# print(info["name"])
# print(info.get("name"))

# info.update({"city": "anuppur"})
# print(info)


# print(info["subjects"]["che"])
# null_dict = {}
# print(null_dict)
# null_dict["name"] = "satya"
# print(null_dict)

# sets

# collection = {1,2,3,3,4,"hello","me"}

# print(collection)
# print(type(collection))
# print(len(collection))

# empty = set()

# empty.add(1)
# empty.add("a")
# empty.add("a")
# empty.add(1)
# empty.add(2)
# empty.add(("p", "q", "r"))

# empty.remove(1)

# print(len(empty))

# empty.clear()
# print(len(empty))
# print(empty)
# print(type(empty))
# print(empty.pop())



# set1 = {1,2,3, 4}
# set2 = {3,4,5}

# print(set1.union(set2))
# print(set1)
# print(set2)
# print(set1.intersection(set2))


# practice questions

# prac = {
#     "table": ["a piece of furniture" "list of facts & figure"],
#     "cat": "a small animal"

# }

# print(prac)

# classroom = {
#     "python", "java", "c++", "python", "js", "python", "java", "c++", "c"
# }

# print(classroom)
# print(len(classroom))



# marks = {}

# a = int(input("enter phy marks :"))
# b = int(input("enter che marks :"))
# c = int(input("enter bio marks :"))

# marks.update({"phy" : a})
# marks.update({"che" : b})
# marks.update({"bio" : c})

# print(marks)


# values = {9, "9.0" }
# print(values)

# val = {
#     ("float", 9.0),
#     ("int", 9)
x = input()
# }
# print(val)


# S = input()

   
# if S[2:] == "nta" and len(S) == 5:
#    print("yes")
# else:
#   print("no")




# T = int(input())



# for _ in range(T):
#   A, B, X, Y = map(int,input().split())
    
# s = A // X 
# total = A + B + s * (Y - X)
# print(total)

# T = int(input())

# for _ in range(T):
#     A, B, X, Y = map(int, input())
    
#     # Number of trades possible
#     trades = A // X
    
#     # Maximum total money after trades
#     total = A + B + trades * (Y - X)
    
#     print(total)


from itertools import count


dict10 = {
"cat" : "a small animal",
"table" : ["a ferniture", "lists of thing in rows and coloumn"]
}
print(dict10)

sub = {
    "python",
    "java",
    "c++",
    "python",
    "javascript",
    "java",
    "python",
    "java",
    "c++",
    "c"
};

print(len(sub))


dict110 = {

}

dict110.update({"phy": 67})
dict110.update({"chem": 97})
dict110.update({"bio": 87})

print(dict110)

values = {
    9, "9.0"
    ("float", 8.0),
    ("int", 9)
}

print(values)






        


    
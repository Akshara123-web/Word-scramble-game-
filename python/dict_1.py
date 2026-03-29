#dict = {"table": ["a piece of furnitures","list of facts and figures"],"cat": "a small animal"}
#print(dict)
list1 = ["python","java","C++","javascript","python","java","python","java","C++","C"]
c=list1.count("C")
cplus=list1.count("C++")
java1=list1.count("java")
python=list1.count("python")
javas=list1.count("javascript")
dict1 = {
    "python": python,
    "C++": cplus,
    "javascript": javas,
    "java": java1,
    "C": c
}
print(dict1)
classroom = list( dict1.keys())
print(len(classroom))
print(classroom)

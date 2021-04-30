print()
print()
print ("__________")
variabletype="int"
print (variabletype)
print ("__________")
a=1
b=a
print(f"initial value of {type(a)} a is {a} with id of {id(a)}")
print(f"initial value of {type(b)} b is {b} with id of {id(b)} ")
a=5
print(f"after change the value of {type(a)} a is {a} with id of {id(a)} ")
print(f"after change the value of {type(b)} b is {b} with id of {id(b)} ")
print(f"Changing a {variabletype} changes id? {id(a) != id(b)}")

print()
variabletype="Float"
print (variabletype)
print ("__________")
a=42.0
b=a
print(f"initial value of {type(a)} a is {a} with id of {id(a)} ")
print(f"initial value of {type(b)} b is {b} with id of {id(b)} ")

a=3.14
print(f"after change the value of {type(a)} a is {a} with id of {id(a)} ")
print(f"after change the value of {type(b)} b is {b} with id of {id(b)} ")
print(f"Changing a {variabletype} changes id? {id(a) != id(b)}")

print()
variabletype="String"
print (variabletype)
print ("__________")
a="That's what I said"
b=a
print(f"initial value of {type(a)} a is {a} with id of {id(a)} ")
print(f"initial value of {type(b)} b is {b} with id of {id(b)} ")

a="Who's on First"
print(f"after change the value of {type(a)} a is {a} with id of {id(a)} ")
print(f"after change the value of {type(b)} b is {b} with id of {id(b)} ")
print(f"Changing a {variabletype} changes id? {id(a) != id(b)}")

print()
variabletype="List"
print (variabletype)
print ("__________")
a= [42, 3.14, 9]
b= a
print(f"initial value of {type(a)} a is {a} with id of {id(a)} ")
print(f"initial value of {type(b)} b is {b} with id of {id(b)} ")

a[2] = "now what"
print(f"after change the value of {type(a)} a is {a} with id of {id(a)} ")
print(f"after change the value of {type(b)} b is {b} with id of {id(b)} ")
print(f"Changing an element in a {variabletype} changes id? {id(a) != id(b)}")
print()
print("assign new list to a")
a= ["forty-two", "3.14", "nein"]
print(f"after change the value of {type(a)} a is {a} with id of {id(a)} ")
print(f"after change the value of {type(b)} b is {b} with id of {id(b)} ")
print(f"Assigning new list to a {variabletype} changes id? {id(a) != id(b)}")




print()
variabletype="Tuple"
print (variabletype)
print ("__________")
a= (42, 3.14, 9)
b= a
print(f"initial value of {type(a)} a is {a} with id of {id(a)} ")
print(f"initial value of {type(b)} b is {b} with id of {id(b)} ")

a= (42, 3.14, "that's what")
print(f"after change the value of {type(a)} a is {a} with id of {id(a)} ")
print(f"after change the value of {type(b)} b is {b} with id of {id(b)} ")
print(f"Changing an element in a {variabletype} changes id? {id(a) != id(b)}")

print()
variabletype ="Dictionary"
print (variabletype)
print ("__________")
a= {"answer":42, "pi":3.14, "number":9}
b= a
print(f"initial value of {type(a)} a is {a} with id of {id(a)} ")
print(f"initial value of {type(b)} b is {b} with id of {id(b)} ")

a["question"] ="?"
print(f"after change the value of {type(a)} a is {a} with id of {id(a)} ")
print(f"after change the value of {type(b)} b is {b} with id of {id(b)} ")
print(f"Adding an element to a {variabletype} changes id? {id(a) != id(b)}")
print()
print("changing element in {variabletype}")
a["question"] ="What do you think"
print(f"after change the value of {type(a)} a is {a} with id of {id(a)} ")
print(f"after change the value of {type(b)} b is {b} with id of {id(b)} ")
print(f"Changing an element in a {variabletype} changes id? {id(a) != id(b)}")
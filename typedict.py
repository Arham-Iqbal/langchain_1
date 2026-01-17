from typing import TypedDict

class Person(TypedDict):
    name:str
    age:int


newperson:Person={'name':"arham",'age':22}

print(newperson)

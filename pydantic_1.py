from pydantic import BaseModel


class User(BaseModel):
    name:str
    age:int

user=User(name="Arham",age=22)

print(user)
print(type(user))

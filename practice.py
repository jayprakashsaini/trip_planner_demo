import json
import ast
import random
a = b'{"email":"thh","password":"rtg"}'
b = a.decode()
print(type(b))
print(b)
a = (1,2,3)
for i in a:
    print(i)

import json

t = "abdegh@gmail.com"
f = dir(t)
if "de" in t:
    print("yessssss")
# print(f)

k = ["abc", "def", "ghi"]
k.remove("abc")
print(k)

l = {"abs":1,"gkk":2}
# l.pop("gkk")
# print(l)
for k,v in l.items():
    print(k)

print(str(random.randint(10000,1000000)))
def create_a_file():
    file_path = r"C:\Users\Jayprakash\Desktop\AppDB\newfile" + str(random.randint(10000,1000000)) + r".txt"
    with open(file_path,'w') as file:
        file.write("uwejsddddddddddddd"*100000)

create_a_file()
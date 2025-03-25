import os
from pathlib import Path

path = Path("requirements.txt")

if os.path.exists(path):
    os.remove(path.parent)

os.system("pip list > "+str(path))
with open(path,"r",encoding = "utf-8") as file:
    req = file.readlines()[2:]

write = []

for i in req:
    write.append(i.split(" ")[0]+"\n")

with open(path,"w",encoding = "utf-8") as file:
    file.writelines(write)

os.system("python -m pip install --upgrade -r "+str(path)+" -i https://pypi.tuna.tsinghua.edu.cn/simple")
os.remove(path)

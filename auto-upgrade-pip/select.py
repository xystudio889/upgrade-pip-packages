import os
from pathlib import Path
from time import time

pip_start_tick = time()

version = "1.0.0"
verText = f"auto-upgrade-pip Version:"+version
news = "更新内容:\n\t存在缓存时可以选择是否保留\n\t更改了缓存目录,现在缓存每次开启电脑时都会刷新"
path = Path("requirements.txt")
print(f"{verText:#^60}\n\n{news}")

pause_time = time()
os.system("pause")
pause_end_time = time()

retain = True

create_cache = time()
if os.path.exists(path):
    while True:
        i = input("检测到缓存存在,请做出选择：\n\tY:保留(不需要创建缓存,有可能不安全)\n\tN:不保留(需要创建缓存,比较安全):")

        if i.upper() == "N":
            os.remove(path)
            break
        elif i.upper() == "Y":
            retain = False
            break
else:
    print("目前没有缓存,正在创建...")

if retain:
    path.parent.mkdir(parents = True,exist_ok = True)
    os.system("pip list > "+str(path))
    with open(path,"r",encoding = "utf-8") as file:
        req = file.readlines()[2:]
    write = []
    for i in req:
        write.append(i.split(" ")[0]+"\n")

    with open(path,"w",encoding = "utf-8") as file:
        file.writelines(write)

create_end_cache = time()

update_time = time()
os.system("python -m pip install --upgrade -r "+str(path)+" -i https://pypi.tuna.tsinghua.edu.cn/simple")

print("正在删除缓存...")

pip_end_time = time()
end_time = time()

print("所有第三方包更新完成.")
print(f"{'时间记录':-^30}")
print("|"+"-"*30+"|")
t1s = f"共用时 : {end_time - pip_start_tick}s"
t2s = f"创建缓存 : {create_end_cache - create_cache}s"
t3s = f"更新包 : {update_time - pip_end_time}s"
print(f'|{t1s: <27}|\n|{30*"-"}|\n|{t2s: <26}|\n|{30*"-"}|\n|{t3s: <27}|\n|{"-"*30}|')

os.system("pause")
os.remove(path)
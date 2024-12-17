import sys
import time
import os

def born_one_son():
    # 如果 "杨老师之子1.py" 不存在，就生成它
    if not os.path.exists("杨老师之子1.py"):
        with open("杨老师之子1.py", "w", encoding="utf-8") as file:
            file.write('print("哇哇哇，要论文")')
        print("杨老师之子1.py 已生成！")
    # 如果 "杨老师之子1.py" 存在，但 "杨老师之子2.py" 不存在，就生成它
    elif not os.path.exists("杨老师之子2.py"):
        with open("杨老师之子2.py", "w", encoding="utf-8") as file:
            file.write('print("哇哇哇，要论文")')
        print("杨老师之子2.py 已生成！")
    # 如果两个文件都存在
    else:
        print("杨老师生不出更多儿子了")

if len(sys.argv) <= 1:
    print("请给杨老师指定工作")
    sys.exit(1)

if  sys.argv[1] == "开组会":
    while True:
        print("动作太慢了啊")

elif  sys.argv[1] == "看开题报告":  
    print("等待杨老师回复中...")
    seconds_in_a_month = 30 * 24 * 60 * 60  # 一个月
    time.sleep(seconds_in_a_month)

elif  sys.argv[1] == "看论文":  
    print("借一下你的一作，下次还你篇好的")

elif  sys.argv[1] == "还钱":  
    print("实验室统筹安排")

elif  sys.argv[1] == "生儿子":  
    born_one_son()

else:
    print("杨老师很忙，请给出杨老师能处理的工作类型")    


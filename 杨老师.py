
import sys
import time

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

else:
    print("杨老师很忙，请给出杨老师能处理的工作类型")    
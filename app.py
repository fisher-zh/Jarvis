import time
from dotenv import load_dotenv
from src.gpts import Jarvis

load_dotenv()

jarvis = Jarvis()

while True:
    user_question = input("请输入您的问题（输入 exit 退出）：")
    # 开始时间
    start_time = time.time()
    # 问答
    if user_question.lower() == "exit":
        break
    result = jarvis.question(user_question)
    # 记录结束时间
    end_time = time.time()
    # 计算执行时间
    execution_time = end_time - start_time

    print(result)
    print(f"耗时: {execution_time:.6f} 秒")

print("Bye~")
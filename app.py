import time
from dotenv import load_dotenv
from src.gpts import Jarvis
load_dotenv()

jarvis = Jarvis()

print("I'm Jarvis, what can I do for you? ")

while True:
    user_question = input("question: \n")
    # 开始时间
    start_time = time.time()
    # 空值直接跳过
    if not user_question.strip():
        continue
    # 退出
    if user_question.lower() == "exit":
        break
    # 帮助命令
    if user_question.lower() == "help":
        print(
            """
            help: 帮助命令
            exit: 退出\n
            """
        )

        continue
    # 问答
    result = jarvis.q(user_question)
    # 记录结束时间
    end_time = time.time()
    # 计算执行时间
    execution_time = end_time - start_time

    # print(f"全部结果: {result}")
    print(f"Time: {execution_time:.6f} s")
    print(f"{result.content}")

print("Goodbye Iron Man")
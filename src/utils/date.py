from datetime import datetime

def get_date():
    # 获取当前日期和时间
    current_time = datetime.now()
    # 格式化输出日期和时间
    formatted_date = current_time.strftime("%Y-%m-%d")
    return formatted_date

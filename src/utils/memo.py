import os
import pandas as pd
from datetime import datetime

# CSV 文件路径
csv_file = os.path.join(os.path.dirname(__file__), "./memo.csv")

# 初始化CSV文件
def initialize_csv():
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["id", "create_time", "content", "execute", "tips"])
        df.to_csv(csv_file, index=False)

# 生成唯一的ID
def generate_id():
    try:
        df = pd.read_csv(csv_file)
        if df.empty:
            return 1
        else:
            return df["id"].max() + 1
    except FileNotFoundError:
        return 1

# 增加备忘录
def add_memo(content, execute, tips=None):
    df = pd.read_csv(csv_file)
    new_id = generate_id()
    create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    new_memo = pd.DataFrame([{'id': new_id, 'create_time': create_time, 'content': content, 'execute': execute, 'tips': tips}])
    df = pd.concat([df, new_memo], ignore_index=True)
    df.to_csv(csv_file, index=False)
    return new_id

# 删除备忘录
def delete_memo(memo_id):
    df = pd.read_csv(csv_file)
    df = df[df["id"] != memo_id]
    df.to_csv(csv_file, index=False)

# 更新备忘录
def update_memo(memo_id, content=None, execute=None, tips=None):
    df = pd.read_csv(csv_file)
    if not df[df["id"] == memo_id].empty:
        if content is not None:
            df.loc[df["id"] == memo_id, "content"] = content
        if execute is not None:
            df.loc[df["id"] == memo_id, "execute"] = execute
        if tips is not None:
            df.loc[df["id"] == memo_id, "tips"] = tips
        df.to_csv(csv_file, index=False)
        return True
    else:
        return False

# 查询备忘录
def query_memo(content=None, execute=None):
    df = pd.read_csv(csv_file)

    # 模糊查询内容
    if content:
        df = df[df["content"].str.contains(content, na=False)]

    # 精确时间查询
    if execute:
        df = df[df["execute"] == execute]

    result = df.to_dict(orient='records')
    return result

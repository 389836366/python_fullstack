print("=== 鹅厂后台：重度玩家净网行动 ===")

# 1. 模拟昨天收集到的玩家数据（我们直接写死一个列表，省得手动输入了）
playtimes = [1.5, 3.2, 0.8, 4.5, 2.0, 5.1, 1.2]

# 准备一个空列表，用来单独关押那些“违规”的玩家
banned_players = []

print(f"今日总共检测了 {len(playtimes)} 名玩家数据。\n")

# 2. 🟢 核心大招：Python的优雅遍历
# 读法：对于 playtimes 列表里的每一个具体时间（我们给它起个临时名字叫 time）
for time in playtimes:
    
    # 在循环内部，加上 if 判断
    if time > 2.0:
        print(f"🚨 抓到违规玩家！游玩时长：{time} 小时。")
        # 把这个违规时长，塞进我们的黑名单列表里
        banned_players.append(time)

# 3. 循环结束，打印战果
print("\n=== 净网行动结束 ===")
print(f"共封禁了 {len(banned_players)} 名玩家。")
print(f"黑名单数据：{banned_players}")
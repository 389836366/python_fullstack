print("=== 鹅厂游戏防沉迷检测系统 ===")
while True:
    try:
        age = int(input("请输入用户的年龄："))
        break
    except ValueError: 
        print("请输入合法的整数")

while True:
    try:
        playtime_hours = float(input("请输入游玩时间："))
        break
    
    except ValueError:
        print("请输入合法的小数！")

if age < 18 and playtime_hours > 1.5:
    print(f"警告：您当前年龄 {age} 岁，已游玩 {playtime_hours} 小时。")
    print("触发未成年人防沉迷机制，账号已被强制下线！去写作业！")
elif age < 18 and playtime_hours < 1.5:
    remaining_time = 1.5 - playtime_hours
    print(f"提示：您当前年龄 {age} 岁。")
    print(f"您还可以继续游玩 {remaining_time:.1f} 小时，请注意休息。")

else:
    print(f"✅ 尊敬的成年玩家，您的防沉迷限制已解除，祝您排位连胜！")

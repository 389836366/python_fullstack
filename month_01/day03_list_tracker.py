print("=== 鹅厂服务器后台：玩家时长统计系统 ===")

playtimes = []

while True:
    user_input = input("请输入玩家游玩时间（输入字母 q 结束录入）：")
    if user_input == "q":
        break

    try:
        time = float(user_input) 
        playtimes.append(time)
        print(f"录入成功！当前已记录{len(playtimes)}名玩家。")

    except ValueError:
        print("输入无效！请输入数字或字母 q。")

print("\n=== 今日数据分析报告 ===")

if len(playtimes) > 0:
    print(f"所有记录明细: {playtimes}")
    print(f"总计肝掉的时长: {sum(playtimes)} 小时")  # sum() 直接求和！
    print(f"最肝玩家时长: {max(playtimes)} 小时")    # max() 直接找最大值！
    print(f"最养生玩家时长: {min(playtimes)} 小时")  # min() 直接找最小值！
else:
    print("今天服务器鬼区了，没有任何记录。")
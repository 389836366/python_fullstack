print("=== 鹅厂游戏：玩家档案数据库管理 ===")

#创建一个玩家字典，冒号左边是key（标签），右边是value（真实数据）
player_profile = {
    "account": "QA_Bot_007",
    "level": 15,
    "is_vip": False,
    "role": "刺客"
}

print("【初始档案已建立】")
print(player_profile)

print("\n=== 玩家行为模拟 ===")

#查：通过key去找value
current_level = player_profile["level"]
print(f"玩家当前等级是: {current_level} 级")

#改：充钱后VIP状态变更
print("玩家充值了 648 元...")
player_profile["is_vip"] = True
player_profile["level"] += 5

# 增：打败了 Boss，获得新装备
print("玩家击败了深渊巨龙...")
player_profile["weapon"] = "屠龙宝刀"

# 3. 打印最终的豪华档案
print("\n【最新豪华档案】")
for key, value in player_profile.items():
    # items() 可以把字典里的 Key 和 Value 一对一对地拿出来
    print(f"{key} : {value}")

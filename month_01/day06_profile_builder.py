def build_profile(name: str, age: int, **kwargs) -> dict:
    print(f"后台收到的必填项：姓名：{name}, 年龄：{age}")
    print(f"双星号kwargs偷偷打包的字典是：{kwargs}")

    #第一步，创造一个基础字典
    profile = {"玩家姓名": name, "玩家年龄": age}
    #第二步，把kwargs这个选填字典，强行塞进我们的基础字典里，用字典的.update()方法，合并两个字典
    profile.update(kwargs)
    return profile

# === 开始测试 ===
print("--- 场景1:只传必填项 ---")
result1 = build_profile("yongyang", 18)
print(f"最终生成的档案1: {result1}\n")

print("--- 场景2:疯狂加戏的选填项 ---")
# 注意看：city, role, weapon 这些参数，我们在函数定义里根本没写！全靠 **kwargs 兜底！
result2 = build_profile("老大哥", 35, city="Shenzhen", role="架构师", weapon="机械键盘")
print(f"最终生成的档案2: {result2}")
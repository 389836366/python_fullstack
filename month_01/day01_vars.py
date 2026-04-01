# Day 01: 变量与交互
# 核心逻辑： 获取输入 -> 存入变量 —> 格式化输出
user_name = input("请输入你的大名: ")
target_job = input("你想进哪家大厂（如：腾讯、华为）：")#其实一家都去不了
target_salary = input("你的期望薪资是多少：")

#打印结果
print("---2027目标已生成---")
print(f"姓名： {user_name}")
print(f"目标：入职{target_job}")
print(f"薪资愿景：{target_salary}")
print(f"加油{user_name}")
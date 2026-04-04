def multiply_numbers(x, y):
    print(f"工厂正在拼命计算 {x} 乘以 {y} ...")
    result = x * y
    return result

print("=== 测试开始 ===")

my_answer = multiply_numbers(5, 8)

print(f"最后的结果是：{my_answer}")

def black_hearted_factory():
    print("黑心工厂：活儿我干了，但我不打算给你任何东西！")

stolen_goods = black_hearted_factory()

print(f"你强行拿到的东西是: {stolen_goods}")
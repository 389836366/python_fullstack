book_name = input("请输入借阅的书名：")
while True:
    try:

        original_price = float(input("请输入书本原价："))
        day_overdue = int(input("请输入逾期天数："))
        break

    except ValueError:
        print("警告：金额或天数必须是数字！别调皮，重新输入！\n")    

fine = original_price * 0.01 * day_overdue

print("--------------------------")
print(f"《{book_name}》借阅结算单")
print(f"书本原价：{original_price}元")
print(f"超期天数：{day_overdue}天")
print(f"您需要缴纳罚金：{fine}元")
print("--------------------------")
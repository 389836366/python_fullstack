print("=== 鹅厂 QA 测试部：批量测试账号生成工具 ===")

#准备一个空列表，用来装生成的账号
test_account = []

for i in range(1,11):
    account_name = f"QA_Bot_{i:03d}"
    test_account.append(account_name)
    print(f"成功生成测试账号：{account_name}")

#循环结束后，打印总览
print(f"\n测试数据生成完毕! 共计{len(test_account)}个账户。") 
print(f"已入库账户列表：\n{test_account}")   
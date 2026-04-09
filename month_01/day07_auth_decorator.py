current_user = {"name": "yongyang", "role": "guest"}

def admin_required(func):
    def wrapper(*args, **kwargs):
        if current_user["role"] == "admin":
            result = func(*args, **kwargs)
            return result
        else:
            print("权限不足")
            return None
    return wrapper

@admin_required
def delete_user_account(user_id: int):
    print(f"正在从数据库中永久拉黑用户{user_id}")

#====开始测试====
print("第一次测试(guest 身份):")
delete_user_account(999)
print("\n------------------------\n")
print("第二次测试(强行把身份改成admin):")
current_user["role"] = "admin"
delete_user_account(999)    
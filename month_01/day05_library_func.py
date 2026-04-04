def calculate_fine(price: float, days: int) -> float:
    print(f"系统正在计算：原价 {price} 元，超期 {days} 天...")
    fine = price * 0.01 * days
    return fine

print("=== 图书馆后台管理系统 ===")
result_fine = calculate_fine(58.8, 10)

print(f"计算完毕，该用户需缴纳罚金：{result_fine}元")   

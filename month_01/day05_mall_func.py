def get_final_price(original_price: float, is_vip: bool = False, promo_code: str = "") -> float:
    """
    计算商城道具最终结算价格。
    包含 VIP 折扣、优惠码扣减及负数价格保底机制。
    """
    final_price = original_price
    if is_vip:
        final_price *= 0.9
    if promo_code == "SZ666":
        final_price -= 50
    if final_price < 0:
        final_price = 0
    return final_price

print("普通玩家买 100 元:", get_final_price(100.0))                           # 预期: 100.0
print("VIP玩家买 100 元:", get_final_price(100.0, is_vip=True))               # 预期: 90.0
print("VIP + 优惠码买 100 元:", get_final_price(100.0, is_vip=True, promo_code="SZ666")) # 预期: 40.0                

    

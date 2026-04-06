def calculate_cart_total(*price: float) -> float:
    """
    计算购物车所有商品的总价。
    *prices 可以接收任意数量的商品价格，并将它们打包。
    """
    print(f"后台收到的商品价格清单：{price}")#打印出来看看它到底变成什么

    total = sum(price)
    return total

print("=== 鹅厂商城购物车结算 ===")

# 场景 1：只买了一瓶水
print("结算 1 件商品:", calculate_cart_total(3.5))

# 场景 2：大佬清空购物车
print("结算 5 件商品:", calculate_cart_total(199.0, 50.0, 29.9, 10.0, 1000.0))

# 场景 3：什么都没买
print("结算 0 件商品:", calculate_cart_total())
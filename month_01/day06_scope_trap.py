player_level = 1
print(f"【系统初始】全服玩家默认等级：{player_level}")
def upgrade_level(current_level: int) -> int:
    new_level = current_level + 1
    print(f"【升级成功】恭喜！当前等级：{new_level}")
    return new_level

player_level = upgrade_level(player_level)    
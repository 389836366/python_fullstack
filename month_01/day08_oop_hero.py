class GameHero:
    def __init__(self, name: str, hp: int):
        self.name = name
        self.hp = hp
        print(f"【系统】英雄 [{self.name}] 初始化完成，血量: {self.hp}")

    def attack(self, target_name: str):
        print(f"[{self.name}] 举起重剑，砍向了 {target_name}！")

    def take_damage(self, damage: int):
        self.hp = self.hp - damage
        print(f"【战报】{self.name} 受到 {damage} 点伤害！剩余血量: {self.hp}")

hero1 = GameHero("亚瑟", 3000)
hero2 = GameHero("鲁班", 1500)

print("\n--- 战斗开始 ---")

# 亚瑟发起攻击
hero1.attack(hero2.name)

# 鲁班挨揍（扣除 500 血）
# 这里的 hero2 就是 self！函数知道改的是鲁班的血，不是亚瑟的。
hero2.take_damage(500)

# 亚瑟也挨揍（扣除 200 血）
hero1.take_damage(200)

class Assassin(GameHero):

    def critical_strike(self, target_name: str):
        print(f"【暴击】[{self.name}] 潜行到 {target_name} 背后，造成了巨额真实伤害！")

    def attack(self, target_name: str):
        print(f"【暗杀】[{self.name}] 掏出淬毒的匕首，悄无声息地划过了 {target_name} 的咽喉！")
            

print("\n--- 第三回合：刺客登场 ---")

hero3 = Assassin("兰陵王", 1200)

hero3.critical_strike(hero2.name)

hero3.attack(hero1.name)

hero3.take_damage(800)
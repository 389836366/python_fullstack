import time  # 导入 Python 自带的时间工具箱

# ==========================================
# 核心组件区：架构师写的“性能雷达”装饰器
# ==========================================
def timer_decorator(func):
    """这是一个装饰器，用来测算其他函数的运行时间"""
    # 仔细看这里！为什么用 *args 和 **kwargs？
    # 因为雷达根本不知道你要测速的函数到底需要多少个参数，所以直接用它们俩把所有可能传进来的参数全兜住！
    def wrapper(*args, **kwargs):
        start_time = time.time()  # 记录开始时间
        
        # 真正去执行被测速的函数，并把参数原封不动地交还给它
        result = func(*args, **kwargs) 
        
        end_time = time.time()    # 记录结束时间
        print(f"【性能雷达】函数 '{func.__name__}' 耗时: {end_time - start_time:.4f} 秒")
        return result
    return wrapper

# ==========================================
# 业务代码区：你写的底层业务逻辑
# ==========================================

# 任务 1：在这个函数头顶上（上一行），加上魔法标签：@timer_decorator
def download_data():
    print("开始下载鹅厂机密数据...")
    time.sleep(2)  # 强制让程序停顿 2 秒，模拟网络延迟
    print("数据下载完成！")

# 任务 2：在这个函数头顶上，同样加上魔法标签：@timer_decorator
def calculate_complex_salary(base: float, bonus: float):
    print(f"开始计算薪资：底薪 {base}, 奖金 {bonus}")
    time.sleep(1)  # 模拟复杂的计算停顿 1 秒
    return base + bonus

# === 开始测试 ===
print("--- 测试 1 ---")
download_data()

print("\n--- 测试 2 ---")
final_salary = calculate_complex_salary(15000.0, bonus=5000.0)
print(f"最终发放到手工资: {final_salary}")
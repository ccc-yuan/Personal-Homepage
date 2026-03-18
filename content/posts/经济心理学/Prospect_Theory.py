import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体（根据系统调整）
plt.rcParams['font.sans-serif'] = ['SimHei']        # Windows 常用黑体
# plt.rcParams['font.sans-serif'] = ['PingFang SC'] # Mac 用苹方
# plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei'] # Linux 用文泉驿
plt.rcParams['axes.unicode_minus'] = False          # 解决负号显示问题

def value(x, alpha=0.5, beta=0.5, lambd=2.5):
    return np.where(x >= 0, x**alpha, -lambd * (-x)**beta)

x = np.linspace(-3, 3, 1000)
y = value(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, linewidth=2.5, label=f'α=β=0.5, λ=2.5')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.xlabel('收益 / 损失 (相对于参考点)', fontsize=12)
plt.ylabel('主观价值', fontsize=12)
plt.title('前景理论价值函数', fontsize=14)
plt.legend()
plt.grid(alpha=0.3)
plt.show()
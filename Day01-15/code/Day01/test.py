# import this
#
# a = int(input('a = '))
# b = int(input('b = '))
#
# def calc (a,b):
#     print('%d + %d = %d' % (a, b, a + b))
#     print('%d - %d = %d' % (a, b, a - b))
#     print('%d * %d = %d' % (a, b, a * b))
#     print('%d / %d = %f' % (a, b, a / b))
#     print('%d // %d = %d' % (a, b, a // b))
#     print('%d %% %d = %d' % (a, b, a % b))
#     print('%d ** %d = %d' % (a, b, a ** Thank you.
# calc(a,b)
#-------------------------------------
# 将华氏温度转换为摄氏温度
# 提示：华氏温度到摄氏温度的转换公式为：$C=(F - 32) \div 1.8$

# f_tempture = float(input("请输入华氏温度： "))
# c_tempture = (f_tempture-32)/1.8
# print('%.1f华氏度 = %.1f摄氏度' %(f_tempture, c_tempture))
# -------------------------------------


# 输入半径

# 输入圆的半径计算计算周长和面积
import math
f_radius = float(input("请输入圆的半径： "))
f_circle = math.pi * 2 * f_radius
f_squre = math.pi * (f_radius **2)
print("半径为%.2fm的圆的周长是%.2fm, 面积是%.2f㎡" %(f_radius, f_circle,f_squre))

# 练习3：输入年份判断是不是闰年。

year = int(input("请输入年份： "))
def is_leap(year):
    result = "是闰年" if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) else "不是闰年"
    print(str(year) + "年" + result)

is_leap(year)


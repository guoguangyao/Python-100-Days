# username = input("用户名： ")
# pwd = input("密  码： ")
#
#
# def check_user_info(username, pwd):
#     result = "身份验证成功！" if username == "admin" and pwd == "123456" else "身份验证失败！"
#     print(result)
# check_user_info(username,pwd)

f_value = float(input("请输入长度： "))
s_unit = input("请输入单位： ")

def switch_unit (f_value, s_unit):
    if s_unit == "in" or s_unit == "英寸":
        print("%.2f英寸 = %.2f厘米" %(f_value, f_value * 2.54))
    elif s_unit == "cm" or s_unit == "厘米":
        print("%f.2厘米 = %f.2英寸" % (f_value, f_value / 2.54))
    else:
        print("请输入有效的单位： ")

switch_unit(f_value, s_unit)
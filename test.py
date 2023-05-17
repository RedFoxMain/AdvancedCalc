# Сделано RedFoxMain
# Github https://github.com/RedFoxMain
from calc import Calc

expression = input(">> ")

obj = Calc()
result = obj.tokinizer(expression)

print(result)


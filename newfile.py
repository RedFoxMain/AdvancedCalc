from calc import Calc

expression = input(">> ")
obj = Calc()
result = obj.tokinizer(expression)
print(result)
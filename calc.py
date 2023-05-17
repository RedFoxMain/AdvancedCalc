# Сделано RedFoxMain
# Github https://github.com/RedFoxMain

import re

def tokinizer(expression):
    tokens = re.split(r'(\^|\+|\-|\*|\/|\(|\))', expression)
    tokens = [t.strip() for t in tokens if t.strip()]
    
    if "(" in tokens:
        opening_index = tokens.index("(")
        closing_index = None
        brackets_count = 0
        
        # ищем закрывающую скобку
        for i in range(opening_index, len(tokens)):
            if tokens[i] == "(":
                brackets_count += 1
            elif tokens[i] == ")":
                brackets_count -= 1
            if brackets_count == 0:
                closing_index = i
                break
        
        # получаем токены внутри скобок и обрабатываем их
        inner_tokens = tokens[opening_index+1: closing_index]
        inner_result = parser(inner_tokens)
        
        # удаляем скобки и их содержимое, добавляем результат
        tokens = tokens[:opening_index] + [inner_result] + tokens[closing_index+1:]
        
        # рекурсивно вызываем функцию для незаконченного выражения
        return tokinizer(" ".join(tokens))
        
    else:
        # обрабатываем токены без скобок
        return parser(tokens)

        
def parser(tokens):
    while len(tokens) > 1:
        try:
            if "/" in tokens:
                try:
                    operator_index = tokens.index("/")
                    left_num = float(tokens[operator_index-1])
                    right_num = float(tokens[operator_index+1])
                    res = left_num / right_num
                    tokens = tokens[:operator_index-1] + [str(res)] + tokens[operator_index+2:]
                except ZeroDivisionError:
                    print("На ноль делить нельзя")
                    break
            elif "*" in tokens:
                operator_index = tokens.index("*")
                left_num = float(tokens[operator_index-1])
                right_num = float(tokens[operator_index+1])
                res = left_num * right_num
                tokens = tokens[:operator_index-1] + [str(res)] + tokens[operator_index+2:]
               
            elif "^" in tokens:
                operator_index = tokens.index("^")
                left_num = int(tokens[operator_index-1])
                right_num = int(tokens[operator_index+1])
                res = left_num ** right_num
                tokens = tokens[:operator_index-1] + [str(res)] + tokens[operator_index+2:]
                    
                  
            elif "+" in tokens:
                operator_index = tokens.index("+")
                left_num = float(tokens[operator_index-1])
                right_num = float(tokens[operator_index+1])
                res = left_num + right_num
                tokens = tokens[:operator_index-1] + [str(res)] + tokens[operator_index+2:]
                
            elif "-" in tokens:
                operator_index = tokens.index("-")
                left_num = float(tokens[operator_index-1])
                right_num = float(tokens[operator_index+1])
                res = left_num - right_num
                tokens = tokens[:operator_index-1] + [str(res)] + tokens[operator_index+2:]
            return tokens[0]
        except ValueError:
            print("Ты точно цифры написал?")
            break
    

    
if __name__ == "__main__":
    while True:
        expr = input(">> ")
        print(tokinizer(expr))

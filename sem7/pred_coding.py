def hello(name):
    return f"Hello, {name}"

def bye(name):
    return f"{name}, bye-bye"

def create_phrase(func):
    name = input("Введите ваше имя ")
    return func(name)

print(create_phrase(hello))
print(create_phrase(bye))

def create_two_phrases(funcs):
    name = input("Введите ваше имя ")
    res = ""
    for func in funcs:
        res += func(name) + "\n"
    return res

# print(create_phrase(hello))
# print(create_phrase(bye))
funcs = (hello, bye)
print(create_two_phrases(funcs))

calculator = {'+': lambda x,y: x + y, 
              '-': lambda x,y: x - y, 
              '*': lambda x,y: x * y, 
              '/': lambda x,y: x / y}

s = input("Введите арифметическое выражение ")
x, op, y = s.split()
print(f"Результат равен {calculator[op] (int(x),int(y)) }")
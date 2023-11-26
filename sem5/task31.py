# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 ...

def fibonachi(n, memo = {}):
    if n in [1, 2]:
        return 1
    if n not in memo:
        memo[n] = fibonachi(n - 1, memo) + fibonachi(n - 2, memo)
    return memo[n]

n = int(input("Enter index of number: "))
print(fibonachi(n, memo={}))
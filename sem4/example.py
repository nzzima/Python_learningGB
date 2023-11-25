def print_sp(sp: list):
    """
    this function print some list
    """
    if not isinstance(sp, list):
        print("Нужен именно список!")
        return
        # raise ValueError("Нужен именно список!")
    for i,v in enumerate(sp):
        print(f"{i=} - {v=}")



sp = [5, 8, 9, True, 'Hello']
s = "Hello"
# print_sp(s)
# print(print_sp.__doc__)
try:
    print_sp(sp)
    print_sp(s)
except ValueError as e:
    print(e)
string = ("She sells sea shells on the sea shore The shells"
          " that she sells are sea shells I'm sure.So if"
          " she sells sea shells on the sea shore I'm sure"
          " that the shells are sea shore shells")
print(len(set(string.replace(".", " ").lower().split())))


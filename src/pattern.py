
for i in range(1, 10):
    #print(" ".join(['*'] * (5 - abs(5 - i))))
    #print(("* " * (5 - abs(5 - i))).strip())
    sep = ""
    for _ in range(5 - abs(5-i)):
        print(f"{sep}*", sep="", end="")
        sep = " "
    print()

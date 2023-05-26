for i in range(6):
    print("*" * 7)


print()


for i in range(5):
    if i == 0 or i == 4:
        print("*" * 5)
    else:
        print("*   *")

for i in range(5):
    spaces = ' ' * (4 - i)
    stars = '*' * (2*i + 1)

    print(spaces + stars + spaces)


"""
4 spacje 1 gwiazdka i = 0 
3 spacje 3 gwiazdki i = 1 
2 spacje 5 gwiazdek i = 2 
1 spajce 7 gwiazdek i = 3 
0 spacji 9 gwiazdek i = 4



"""
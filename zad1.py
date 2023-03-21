def zad1():
    x1 = "python2023"
    x2 = "python2023"
    x3 = "python2023"

    print(x1 == x2)
    print(x2 == x3)

    print(type(x1), hex(id(x1)))
    print(type(x2), hex(id(x2)))
    print(type(x3), hex(id(x3)))

    x3 = "java11"

    print(x1 == x2)
    print(x2 == x3)

    print(type(x1), hex(id(x1)))
    print(type(x2), hex(id(x2)))
    print(type(x3), hex(id(x3)))

    zad1()
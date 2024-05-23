def isQrty(x, y):
    """

    :param x:
    :param y:
    :return:
    """
    if x > 0 and y > 0:
        return 1
    elif x > 0 and y < 0:
        return 2
    else:
        return 0;

def testList():
    """

    :return:
    """
    # list
    lst = [1, 2, 3]
    if lst:
        print("hello 4")
    print(type(lst))
    lst.append(True)
    print(lst)
    lst.clear()
    print(lst)
    print(type(lst))
    lst.append(True)
    print(lst)
    lst.clear()
    print(lst)
# asd
def testTernar():
    """

    :return:
    """
    # ternar
    a = 20
    b = "True" if a > 10 else "False"
    print(b)

def testTuple():
    tuple1 = (1, 2, 3)
    print(tuple1)
    tuple1 = "asd"
    print(tuple1)
    tuple2 = (1, 2, [3, 3])
    print(tuple2)
    tuple2[2].append("appended")
    print(tuple2)
    tuple3 = tuple([1])
    print(tuple3)



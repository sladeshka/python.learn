import math
import math as m
from math import pi, sin
import exp_mod
def testOne():
    SECS_IN_MIN = 60
    s1 = "Hello"
    s2 = "Hell" + "o"
    print(f"{s1 == s2} {s1 is s2}\n")
    # o = input("Enter a character => ")
    o = "o"
    s3 = "Hell" + o
    print(f"{s1 == s3} {s1 is s3}\n")
    print("\t\tHello\n\nWorld")

    # t = input("Enter time period in minutes =>")
    t = "1"
    print(f"Your time is {t * SECS_IN_MIN} seconds")
    print(f"Your time is {int(t) * SECS_IN_MIN} seconds")
    print(f"Your time is {int(t) ** SECS_IN_MIN} seconds")
    print(r"Your time is {int(t) ** SECS_IN_MIN} seconds")
    print(b"Your time is {int(t) ** SECS_IN_MIN} seconds")
    print(u"1")
    print(math.pi)
    print(m.pi)
    print(sin(pi))
    print(exp_mod.pi)
    print(f"{math.pi:.2f}")
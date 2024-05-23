from lesson2_mod import testOne
from lesson3_mod import isQrty, testList, testTernar, testTuple

# lesson 2
testOne()
# test
переменная = "123"
locals()[f'переменная{переменная}'] = 123
print(переменная123)
# lesson 3
qrty = isQrty(1, 2)
print(qrty)
testList()
testTernar()
testTuple()

lst=[1,2,3]
lst = lst[1:2:2]
print(lst)
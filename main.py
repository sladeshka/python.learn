from lesson2_mod import testOne
from lesson3_mod import isQrty, testList, testTernar, testTuple
from lesson4_mod import testReadWrite, read_zip_all, calculate_distance

# # lesson 2
# testOne()
# # test
# переменная = "123"
# locals()[f'переменная{переменная}'] = 123
# print(переменная123)
# # lesson 3
# qrty = isQrty(1, 2)
# print(qrty)
# testList()
# testTernar()
# testTuple()
#
# lst=[1,2,3]
# lst = lst[1:2:2]
# print(lst)
#
# testReadWrite()
#
# read_zip_all()
#
# distance = calculate_distance([1, 1], [2, 2])
#
# print("ASDASDASDASD"+distance)


lat = 40.7128
lon = -74.0060

formatted_lat = '{:.4f}'.format(lat)
formatted_lon = '{:.4f}'.format(lon)

print('Широта: {}'.format(formatted_lat))
print('Долгота: {}'.format(formatted_lon))
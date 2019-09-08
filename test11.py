list1=[123,234]
list2=[234,345]
list3=[123,234]
# print(list1<list2, list1==list3)
list4 = []
list4.extend(list1)
list4.extend(list3)
print(list4)
# list3 *= 3 #list3= list3*3
# print(list4<list2)
# print(list1,list2,list3,list4)
# #列表内是否存在
# print(123 in list1,123 not in list1)
list5 = [111,222,[111,222,333,'小甲鱼']]
list6 = list5*5
print(333 in list5, 333 not in list5)
print('小甲鱼' in list5[2])
print(list6.count(111))
print(list6.index(222,3,7))
member = ['小甲鱼', '小布丁', '喜羊羊', '灰太狼', "冬瓜香蕉牛奶东方明珠塔"]
TTC= member
# TTC = member.reverse()

# print(member.reverse())
member.reverse()

print(TTC)
print(member)

list7 = [4,5,8,6,3,2,1,6,3,2,4,66,2,1,4,6,]
list7.sort(reverse=True)
print(list7)

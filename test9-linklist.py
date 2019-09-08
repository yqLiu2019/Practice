member = ['小甲鱼', '小布丁', '喜羊羊', '灰太狼', "冬瓜香蕉牛奶东方明珠塔"]
number = [1,2,3,4,5]
mix = [1, '小甲鱼', 3.14,[1,2,3]]
empty = [] #空列表
for i in member:
    print(i)
for i in mix:
    print(i)
#member.append('PDD')
mix.append([3,4,5])
mix.extend([111,222])
mix.insert(0, '牡丹')
#print(len(member))
for i in mix:
    print(i)
member = ['小甲鱼', '小布丁', '喜羊羊', '灰太狼', "冬瓜香蕉牛奶东方明珠塔"]
member[0], member[1]= member[1], member[0]
print(member)
member.remove('小布丁')
print(member)
del member[0]
print(member)
name = member.pop()
print(member.pop())
print(name)
print(member)
member = ['小甲鱼', '小布丁', '喜羊羊', '灰太狼', "冬瓜香蕉牛奶东方明珠塔"]
print (member[2:])
member2 = member#赋值 传地址式赋值
member3 = member[:]#拷贝
member.remove("小布丁")
print(member2)
print(member3)

# 处理列表的部分元素——Python称之为切片

players=['lindan','malong','lizongwei','chenglong']
print(players[1:3])# ['malong', 'lizongwei']
print(players[:3])# ['lindan', 'malong', 'lizongwei']不指定开始就从最开始开始
print(players[2:])# ['lizongwei', 'chenglong'] 不指定结束就到最后
print(players[-2:])# ['lizongwei', 'chenglong']从倒数第二个到最后
print(players[:-2])# ['lindan', 'malong'] 从第一个到倒数第二个

# 遍历切片

for player in players[:2] :
    print(player.title())

#
scores=[100,65,34,78,66,25,98,76,53,99,27]
temp=sorted(scores,reverse=True)
print(temp)
for score in temp[:3] :
    print(score)
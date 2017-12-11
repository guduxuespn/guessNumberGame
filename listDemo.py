#演示表达式的一个例子
#[ (x,y) for x in [1,2,3,4] for y in [3,4,5,6] if x != y]

#[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

list_resault =[ (x,y) for x in [1,2,3,4] for y in [3,4,5,6] if x != y]
print (list_resault)
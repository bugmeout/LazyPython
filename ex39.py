ten_things = "Apple Orange Crows Telephone Light Sugar"

print "Wait there's no 10 things in that list, let's fix that."

stuff = ten_things.split(" ")
more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]

while len(stuff) != 10 :
	next_one = more_stuff.pop()
	print "Adding:",next_one
	stuff.append(next_one)
	print "There's %d items now." %len(stuff)
	
print "There we go:",stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()

print ' '.join(stuff)
print '#'.join(stuff[3:5])



#1.
#more_stuff.pop()先出来的是“boy”,也就是list是堆栈结构，index[0]是栈底
#这也是pythonList的牛逼之处，存储是堆栈存储，但是还是可以随机存取
#
#2.
#stuff[-1]
#这个很爽。表示倒数第几个元素，记住，是从1开始，而不是0开始。
#
#3.
#''.join(stuff),得到的结果是个字符串，而不是让stuff的每个元素都加上个' '.
#测试后，发现stuff没有变化，故join操作属于读取操作，不是修改操作。当然，指的是针对
#原来的东西
#
#4.stuff[3:5]
#表示从index3开始，5之前的元素，(不包括index5啊，记住了)
#为什么是下一个序号呢，这是为了由5-3=2直接得出输出2个元素。数数的问题。
#一般可以这么利用，stuff，第一个元素的索引，然后考虑输出几个，然后再加数字就行了。
#所以来理解，stuff[0,len(stuff)]
#表示，从0元素开始，一共输出len(stuff)个元素
#其实说穿了，就是全部输出的意思。
#因为len(stuff)-1的结果就是列表最后一个元素的索引。
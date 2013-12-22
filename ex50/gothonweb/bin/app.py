#coding:utf8--
import web
urls = ('/', 'index','/test','test','/good','good','/another','another')
#注意python元组的对应关系

 
app = web.application(urls,globals())

#render = web.template.render('templates/')
#app can find teplates from the render path metioned here.
render2 = web.template.render('templates/')

#different file should use different class.
#lib using the urls PAIR translate into class KEY WORDS.
#just as :
#Visitor request /test . APP using the URLS PAIRS METIONED 3rd line.
#Change /test into string "test".

class index:
	def GET(self):
		greeting ="hello world!"
		fool ="I am fool"
		#return greeting
		#
		#The next sentence means you should load file.
		#the work belong to render2.
		#render2 WHERE FIND FILES: "templates/"  11th line.
		#render2 FIND WHICH FILE
		#		NAMED foo.html   --> render2.xxx(para1 list)
		# With Paramater (fool),the value is fool string.
		return render2.foo(fool = fool,greeting = greeting)
		#return render.index(greeting = greeting)

class test:
	def GET(self):
		sayhello = "i am hello"
		return render2.foo(fool = sayhello)

class good:
	def GET(self):
		good = "good enough"
		greeting = good
		return render2.index(greeting)

#version 2.0  add web input function
class another:
	def GET(self):
		#str数组接受输入，其中funny的默认值为"wahahah"
		#这里的输入是通过url输入的
		#变量前加？而且变量赋值等号两端不能有空格
		#http://localhost:1234/another?test=wa
		#http://localhost:1234/another?test = wa (WRONG)
		str = web.input(funny ="default")
		# str应该是个字典,而且不只是个字典，因为字典没有dic.attri方法
		# 下面两个if都是一个效果，60行的更直观一些
		# if 'test' in str 是说字典str中有没有test属性，其实就是问str中有没有以test作为索引的key。
		#dictionary .........[index][key].......
		#http://localhost:1234/another?tes=me&test=wahah
		if 'test' in str:
		#if str.has_key('test'):
			return render2.index(str.test)
		else:
		#http://localhost:1234/another?tes=me&wa=test&funny=100
			return render2.index(str.funny)


		
if __name__ == "__main__":
	app.run()
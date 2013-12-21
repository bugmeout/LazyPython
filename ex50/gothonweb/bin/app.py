#coding:utf8--
import web
urls = ('/', 'index','/test','test','/good','good')
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
		#		NAMED foo.html    render2.xxx(para1 list)
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
		return render2.index(greeting = good)

		
if __name__ == "__main__":
	app.run()
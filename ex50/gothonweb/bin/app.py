import web
urls = ('/', 'index','/test','test','/good','good')
#注意python元组的对应关系

 
app = web.application(urls,globals())

#render = web.template.render('templates/')
render2 = web.template.render('templates/')

class index:
	def GET(self):
		greeting ="hello world!"
		fool ="I am fool"
		#return greeting
		return render2.foo(fool = fool)
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
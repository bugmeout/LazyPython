#--coding:utf8--


#注意，在python中，None和''不是一个意思
#但是二者的逻辑表达式都为false
#a = None
#b = ''
#if(a) 与if(b)都是False
import web
#urls = ('hello/','Index')
urls = ('/hello','Index','/test','test','/postway','postway')
app = web.application(urls,globals())

render = web.template.render('templates/',base='layout')

class Index():
	def GET(self):
		form = web.input(name = "Nobody")
		#greeting = "Hello,%s,%s" % form.name,form.greet
		#if 'greet' in form and not(form['greet'] is None)
		#如果用上面的这句判断
		#http://localhost:8080/hello?name=Nancy&greet=
		#if判断会是成功的
		#因为url中的greet=，不代表from['greet'] is None 
		#而代表的是form['greet'] = ''，未输入时候的默认值
		if 'greet' in form and not (form['greet'] == ''):
			greeting = "hello %s,%s" %(form.name,form.greet)
		else:
			greeting="fuck ,%s" % form.name

		return render.index(greeting = greeting)


class test(object):
	def GET(self):
		str = web.input(name='cang',greet =None)
     #testEx1:http://localhost:8080/test?greet
		#if str.greet=='':
		if str.greet:
			greeStr = "%s,%s" %(str.name,str.greet)
			return render.index(greeStr)
		else:
		#	return str 
		#<Storage {'name': 'cang', 'greet': None}>
		#None is NOT ''  ----------:-)
		#哈哈，将来可以使用这个方法来调试了。
		#因为这里的return就return给了浏览器
			return "Error: greet is required."


class postway(object):
	def GET(self):
		return render.hello_form()
	def POST(self):


		#How to receive the posted data.........





		#this sentence is meaningless.
		record = web.input(name='Nobody', greet = 'Hello')
		greeting = "%s,%s" % (record.name,record.greet)
		return render.index(greeting = greeting)		





if __name__ == "__main__":
	app.run()
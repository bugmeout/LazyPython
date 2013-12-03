
from sys import argv
script , user_name = argv
prompt ='>'

print "Hi, %s, I'm the %s script." %(user_name,script)
print "I'd like to ask you a few quesitons."
#在这句加逗号的目的是为了不换行，原来python中，默认print完毕之后会换行，加上逗号就可以消除影响了
print "Do you like me %s?" %user_name ,
#likes = raw_input(prompt),            加逗号没用，在输入完毕之后，会永远的另起一行。
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r , Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
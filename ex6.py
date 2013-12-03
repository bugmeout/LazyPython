x = "There are %d types of people." % 10
binary = 'binary'
do_not = "don't"
y = "Those who know %s and those who %s." %(binary,do_not)

print x
print y

#what's the meaning of%r.万能格式匹配符，而且带有类型信息如输出false之类。
#好牛逼。

print "I said: %r." %x
print "I also said: '%s'." %y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
#That's a speical way to show format string .
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
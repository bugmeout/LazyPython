tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

test = "I am 6'2\" tall."
print test

test2 ='I am 6\'2" tall.'
print test2
#back-slash 后面的东西代表不是真实字符串意思，\' 表示输出',     \"表示输出"




print tabby_cat
#	I'm tabbed in.
# Tab space is "		", not "	" in python.
print persian_cat
#I'm split
#on a line.	
print backslash_cat
#I'm \a \cat.
print fat_cat
#I'll do a list:
#	*Cat food
#	*Fishies
#	*Catnip
#	*Grass
# * is a normal char.
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL_C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename,'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now i'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write('\n')
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#txt = target.read()
#print txt
#the sentence is wrong, that shows FILE NOT OPEN FOR READING. because you open the file for writing.
#还有一点，就是如果输入了\n,python往文件里面写的时候不会换行，他会把你所有的输入都当做字符，防止了注入类问题的发生。
print "And finally, we close it."
target.close()
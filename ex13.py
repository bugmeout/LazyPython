from sys import argv

script ,first,second,third = argv

print "The script is called:", script
print "Your first variable is :", first
print "Your second variable is :", second
print "Your third variable is: ", third


#notice:
# script ,first,second,third = argv MEANS script = argv[0],first= argv[1]......
#script ="1",second ="2" IS WRONG ,MUST BE script ="1" second = "2",不能有逗号，否则会提示错误
#
#
#
#
#
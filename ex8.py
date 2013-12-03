#--coding:utf-8--
bingo = "%r %r %r %r"

print bingo % (1,2,3,4)
print bingo % ("one", "two","three","four")
print bingo % (bingo,bingo,bingo,bingo)
print bingo % (
	"I had this things.",
	"That you could type up right",
	"But it didnt sing.",
	"So I said goodnight."
)

#if i change the last sentence "but it didn't sing."
#the screen will show "but it didn't sing."  NOT 'but it did' t sing'.
#Just as you see,单引号的出现如果还是按照之前的输出的话(单引号出来句子),就明显有逻辑错误。enheng........

#print test
#报错，提示undefine test.
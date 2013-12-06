
from sys import exit
from random import randint

class Game(object):
	def __init__(self,start):
		self.quips = [
		"You died.",
		"Your mom will be proud",
		"Such a loser.",
		"I have a small puppy that's better than this."
		]
		
		self.start = start
		
	def play(self):
		next = self.start
		
		while True:
			print "\n----"
			room = getattr(self,next) 
			next = room() 
	

	def death(self):
		print self.quips[randint(0,len(self.quips)-1)]
		exit(1)
		
	def central_corridor(self):
		print "Central_Corridor"
		print "You should take action!"
		
		action = raw_input("> ")
		
		if action =="shoot":
			print "You action is shoot.YOu died"
			return 'death'
		
		elif action == "dodge":
			print "you action is dodge.You died"
			return 'death'
		
		elif action == "tell a joke":
			print "You killed him when the man was laughing."
			return 'laser_wepon_armory'
		
		else:
			print "fuck off,the chinese was not recognized."
			return 'central_corridor'
			
	def laser_wepon_armory(self):
		print "You should guess a number"
		code = "%d%d%d" %(randint(1,9),randint(1,9),randint(1,9))
		guess = raw_input("[Keypad]> ")
		guesses = 0
		
		while guess != code and guesses < 10:
			print "Go on!"
			guesses += 1
			guess = raw_input("[Keypad]> ")
		
		if guess == code:
			print "Got it. you should go to the bridge"
			return 'the_bridge'
		else:
			print "BaGaYaluuuu.you stupid,U DIED"
			return 'death'
		
	def the_bridge(self):
		
		action = raw_input("What you should do? >")
		
		if "throw" in action:
			print "TOO early, you was discovered,died"
			return 'death'
		
		elif "slow" in action:
			print "You got it .next mission is escape the pod"
			return 'escape_pod'
			
		else :
			print "die"
			return 'the_bridge'
			
	def escape_pod(self):
		print "You shuld pick up one boom  1~5"
		good_pod = randint(1,5)
		guess = raw_input('guess')
		
		if int(guess) != good_pod:
			print "fuck ouff"
			return 'death'
		else:
			print "woca, You Win!"
			exit(0)

a_game = Game('central_corridor')
a_game.play()

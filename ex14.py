from sys import argv

#'''
#import time
#import sys

#def delay_print(s):
#    for c in s:
#        sys.stdout.write( '%s' % c )
 #       sys.stdout.flush()
 #       time.sleep(0.10)
#'''

script, user_name = argv
prompt = '> '

print("Hi %s, I'm the %s script." % (user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % user_name )
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of cpmputer do you have"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
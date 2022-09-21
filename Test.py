# import subprocess

# search = 'cheeseburger'
# args = ['open','dict://'+search]
# subprocess.Popen(args)

#import macdict
from macdict import lookup_word

definition = lookup_word(u'physical')
print(definition)

#macdict.lookup_word("Xin chào")

print("Heloo")
# Alex Hicks (awh4kc)
# Sonia Foley (sf3be)

import random

question = input("What question do you wish to ask the 8 ball? ")
print("You asked the 8 ball:", question)

eight_ball_list =  ['Whatever, who cares?', 'That is not the question you should be asking', 'Most likely', 'Ask again later', 'Cannot predict now',
                    'My reply is no', 'Very doubtful', 'My dog ate the answer', 'As I see it, yes', 'Probably, I do not care', 'Of course you nincompoop',
                    'All signs point to yes', 'Concentrate and ask again', 'Better not tell you now', 'My sources say no', 'You wish']

rand_answer = eight_ball_list[random.randint(0, len(eight_ball_list)-1)]

print("The 8 ball says: ", rand_answer)


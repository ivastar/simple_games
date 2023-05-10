import random

correct_path = 'wwnneseenessswses'

CHOICES = 'nesw'

def get_player_choice():
    """Get user input and validate it is one of the choices above"""
    player_choice = None
    while player_choice is None:
        player_choice = input('Choices: \n(N)orth \n(W)est \n(S)outh \n(E)ast \n\nPick: ')
        if player_choice.lower() not in CHOICES:
            player_choice = None
    return player_choice.lower()

incorrect_paths = ['Oh! There is a minotaur down this way! He smells bad. You may consider a different path',
'You run into sirens and begin to be hypnotized by their song. You plug your ears and quickly choose another path',
'You bonk your head on a wall! How stupid! Pick a different path.',
'You feel the temperature dramatically rise and you see an emerald dragon breathe flames before your very eyes! Run a different direction.',
'There is a pool here and in it is a shark with laser beams attached to its head!! Dodge the lasers and scary bite and go a different direciton.',
'There are thousands of hairy spiders each with ten eyes that begin to crawl over you! Shake them off and go a different direction.']

def labyrinth():
	i=0
	print('You wake up in a dark, foggy labyrinth...you are thirsty, freezing, and need to find your way out as quickly as possible. There is only one correct path')
	while i < len(correct_path):
		print('Which direction do you want to go?')
		player_choice = get_player_choice()
		if player_choice == correct_path[i]:
			print('You feel one step closer to freedom!')
			i+=1
		else:
			print(incorrect_paths[random.randint(0,5)])
	print('You narily escaped the dangerous labyrinth! Now you can rest in a nearby hammock :)')

if __name__ == "__main__":
    labyrinth()



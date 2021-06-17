import random
def main():
	dice_rolls = 2
	die_sum=0
	for i in range(0,dice_rolls):
	 	roll = random.randint(1,6)
	 	die_sum+=roll
	 	print(f'You rolled a {roll}')
	print(f'You have rolled a total of {die_sum}')


if __name__== "__main__":
  main()
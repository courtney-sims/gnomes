class Gnomes():
	def __init__(self):
		self.offerings = {
			"blanket" : 1,
			"wrap" : 1,
			"bow" : -1,
			"cozy": 1,
			"green": 1,
			"plant": 1,
			"flower": 1,
			"soup": 1,
			"coffee": 3,
			"tea": 3,
			"socks": 2,
			"hat": 3,
			"phone": -3,
			"battery": -3,
			"jewel": 3,
			"stone": 2,
			"precious": 3,
			"gem": 3,
			"sun": 1,
			"pie": 2,
			"stew": 1,
			"fuzzy": 1
		}
	def check_appeasement(self, score):
		if score > 0:
			return True
		else:
			return False
	
	def calculate_score(self, offering):
		total = 0
		for word in offering.split():
			if word in self.offerings:
				total += self.offerings[word]
		return total

	def get_input(self):
		return input("Happy Winterfest to you! Please describe your offering.\n")

	def output(self, appeasement):
		if appeasement:
			return "I am appeased."
		else:
			return "I am not appeased"

if __name__ == '__main__':
	gnome = Gnomes()
	offering = gnome.get_input()
	score = gnome.calculate_score(offering)
	is_appeased = gnome.check_appeasement(score)
	print(gnome.output(is_appeased))

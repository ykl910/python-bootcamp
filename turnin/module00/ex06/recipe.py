cookbook = {}
Sandwich = {
	"ingredients": ["ham", "bread", "cheese", "tomatoes"],
	"meal": "lunch",
	"prep_time": 10
}

Cake = {
	"ingredients": ["flour", "sugar", "eggs"],
	"meal": "dessert",
	"prep_time": 60
}

Salad = {
	"ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
	"meal": "lunch",
	"prep_time": 15
}

cookbook["Sandwich"] = Sandwich
cookbook["Cake"] = Cake
cookbook["Salad"] = Salad

def printName():
	for key, value in cookbook.items():
		print(key)

def printRecipe():
	name = input("Enter recipe name to print: \n")
	for key in cookbook:
		if name == key:
			recipe = cookbook[name]
			for key, value in recipe.items():
				print(f"{key}:{value}")

def removeRecipe():
	name = input("Enter recipe name to remove: \n")
	for key, value in cookbook.items():
		if name == key:
			cookbook.pop(name)
			break

def addRecipe():
	name = input("Enter recipe name: \n")
	print("Enter ingredients: ")
	ingredients = []
	while True:
		ingredient = input()
		if ingredient == "":
			break
		ingredients.append(ingredient.strip())
	meal = input("Enter meal type\n")
	while True:
		try:
			prep_time = int(input("Enter preparationt time\n"))
			break
		except ValueError:
			print("prepartion time not valid")

	new_recipe = {
		"ingredients": ingredients,
		"meal": meal,
		"prep_time": prep_time	
	}
	cookbook[name] = new_recipe


if __name__ == "__main__":
	print("""Welcome to the Python Cookbook !
List of available options:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit\n""")
			
	while True:
		while True:
			try:
				option = input("Please select an option\n")
				op = int(option)
				break
			except:
				print("""Sorry, this optiondoes not exist.
List of available options:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit\n""")
		
		if op == 1:
			addRecipe()
		elif op == 2:
			removeRecipe()
		elif op == 3:
			printRecipe()
		elif op == 4:
			printName()
		elif op == 5:
			print("Cookbook closed. Goodbye !")
			exit(0)
		else:
			print("""Sorry, this optiondoes not exist.
List of available options:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit\n""")

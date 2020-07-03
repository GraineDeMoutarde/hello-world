

def parseDaily():
	text = open('daily.txt', 'r')
	text.close()
	return [{"nom": "sport", "debut": "05h00", "fin": "06h00"}]

planning = parseDaily()

def checkinterval_df(newtask):
	for task in planning:
		if "debut" in task.keys() and newtask["debut"] < task["debut"] < newtask["fin"]:
			return False
		if "fin" in task.keys() and newtask["debut"] < task["fin"] < newtask["fin"]:
			return False
		if "debut" in task.keys() and "fin" in task.keys() and newtask["fin"] > task["debut"] and newtask["debut"] < task["fin"]:
			return False
	return True

def checkinterval_d(newtask):
	for task in planning:
		if "debut" in task.keys() and "fin" in task.keys() and task["debut"] < newtask["debut"] < task["fin"]:
			return False
		if "fin" in task.keys() and task["fin"] > newtask["debut"]:
			return False
	return True

def checkinterval_f(newtask):
	for task in planning:
		if "debut" in task.keys() and "fin" in task.keys() and task["debut"] < newtask["fin"] < task["fin"]:
			return False
		if "debut" in task.keys() and task["debut"] < newtask["fin"]:
			return False
	return True


def ajouter():
	newtask = {}

	print("Ajout d'un élément")
	nom = input("nom: ")
	newtask["nom"] = nom

	choixinterval = 0
	while choixinterval == 0:
		print("Autres paramètres (debut, fin)")
		params = input("").split(", ")
		if len(params)==1:
			break
		for p in params:
			key, value = p.split(": ")
			newtask[key] = value

		if "debut" in newtask.keys() and "fin" in newtask.keys():
			if checkinterval_df(newtask):
				choixinterval = 1

		if "debut" in newtask.keys() and "fin" not in newtask.keys():
			if checkinterval_d(newtask):
				choixinterval = 1

		if "debut" not in newtask.keys() and "fin" in newtask.keys():
			if checkinterval_f(newtask):
				choixinterval = 1


	planning.append(newtask)
	print(newtask)




def retirer():
	pass

daily = parseDaily()


width = 35


def display_roll():
	for k in range(8,15):
		display_content(k)
		print(" " * width)
		print(" " * width)
		print(" " * width)


def display_content(k):
	time  = str(k) + "h"
	time2 = str(k+7) + "h"
	print(time + " titre" + " " * (width -(len(time + " titre"))) 
		+ time2 + " titre2" + " " * (width -(len(time2 + " titre2"))))

display_roll()

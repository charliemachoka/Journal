import main

def view_entries():







	print("Date\t\tTitle\t\tBody")
	n = 1
	for entry in main.journal:
		date = entry.keys()[0]
		print(n, " ",  date , "\t\t", entry[date]['title'], "\t\t", entry[date]['body'])
		n = n+1

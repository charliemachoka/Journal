
import main

def create_new_entry():
	title = raw_input ("Please enter title: ")
	body = raw_input("Please enter the body: ")
	journal_date = raw_input("Enter the date (year-month-day): ")

	
	inner = {}
	inner['title'] = title
	inner['body'] = body
	new_entry = {}
	new_entry[journal_date] = inner

	main.journal.append(new_entry) 

# Main program


import menu
import new_entry
import delete_entry


#import file_operations


journal = []
# file_operations.loadJournal()

def main():
	# prommpt for main
	menu.intro()	

	while True:
		user_input  = menu.menu()
		if user_input == 1:
			# create new entry
			new_entry.create_new_entry()
		elif user_input == 2:
			# view last entry
			# FORMAT THIS!!!!!
			print(journal[-1])
		elif user_input == 3:
			delete_entry.delete_entry()
		elif user_input == 4:
			#file_operations.saveJournal()
			print("\n\nGoodbye .... ")
			break



if __name__ == '__main__':
	main()



				


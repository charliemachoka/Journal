def intro():
    print ('\t ')
    print ("\t\t __ __   __        __       _")
    print ("\t\t   |    |  | |  | | _||\ | /_\  |    ")
    print ("\t\t __|    |__| |__| | | | \|/   \ |__  ")
    print ('-------------------------------------------------------------------------')
    print ('\t\t Hello, Welcome to your journal')
    print ('\t Simple console app to collect your thoughts and events')
    print ('. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ')
    print ('-------------------------------------------------------------------------')


def menu():
    name = input("Hey, what\'s your name?")
    print(name + "!!" + " welcome to your journal")
    print("What would you like to do today?")
    print("1: To Create your a new journal enter '1' ")
    print("2: To make A new Entry enter ")
    print("3: To view your last Journal Entry enter")
    print("4: To delete entries")
    print("5: To exit enter")
    user_input = input('')

    if user_input == '1':
        print("hey")
intro()
menu()


        
    

               
               
               
               
               

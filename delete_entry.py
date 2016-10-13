import viewentries
import main
def delete_entry():
    """delete a journal created before"""
    viewentries.view_entries()
    choice = int(input("Enter the journal number to delete: "))


    del(main.journal[choice - 1])

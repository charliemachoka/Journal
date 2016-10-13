
import pickle

# assumes the variable journal
def saveJournal():
	with open('journalFile', 'wb') as f:
		pickle.dump(journal, f)

def loadJournal():
	with open('journalFile', 'rb') as f:
		journal = pickle.load(f)

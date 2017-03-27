

import textindex
lu=raw_input('Enter Word,separate multiples with a comma: ')
def search(lu):
	index = textindex.Index()
	index.print_lookup(lu)
search(lu)

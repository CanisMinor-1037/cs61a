from unicodedata import lookup

suits = ['heart', 'diamond', 'spade', 'club']
print([lookup('WHITE ' + s.upper() + ' SUIT') for s in suits])

from re import fullmatch
match1 = fullmatch(r'(?P<name>\w+) (?P<surname>\w+)', 'Timur Guev')
kk(match1.groupdict())

import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
is_valid = False

checks = {'upper': False, 'lower': False, 'number': False, 'character': False}

# Do all the requirement checks here.
if 6 <= len(password)  <= 16:
    for l in password:
        if l.islower():
            checks['lower'] = True
        elif l.isupper():
            checks['upper'] = True
        elif l.isnumeric():
            checks['number'] = True
        elif l in "$#@":
            checks['character'] = True

print(is_valid)

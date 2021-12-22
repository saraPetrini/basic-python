import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
is_valid = False

# Do all the requirement checks here.
has_lower = False
has_upper = False
has_number = False
has_special = False
has_right_length = 6 <= len(password) <= 16

for a in password:
    if a.islower():
        has_lower = True
    if a.isupper():
        has_upper = True
    if a.isnumeric():
        has_number = True
    if a in '$#@':
        has_special = True


is_valid = has_lower and has_upper \
    and has_number and has_special \
    and has_right_length

print(is_valid)

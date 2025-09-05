
# You should write a loop around this question, and keep asking until
# the answer is "yes" (lower case).

stop = False 
while (not stop):
    print("inside")
    stop = (input('Do you want to stop? yes or no')) == "yes"

print("out")
camel = str(input("What is the name of your variable in camel case "))
camel = camel.lower()
camel = camel.replace(" ", "_")
print("You're variable's name in snake case is " + camel)
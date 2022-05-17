# Demonstration of f-strings

first_name = "Tom"
last_name = "Brady"
full_name = f"The oldest player in the leageu is {first_name} {last_name}."
print(full_name)

print("\tIndent")
print("Players:\n\tLeonard Fournette\n\tRonald Jones II\n\tAntonio Brown (bitch boy)")

dumb_input = "  Answer   "
print(dumb_input.rstrip() + "See?")
print(dumb_input.lstrip() + "See?")
print(dumb_input.strip())

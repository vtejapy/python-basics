#REMINDERS APP
shopping_list = []

# Print shopping_list
def printer():
    print("Here's your list")
    print('\n')
    for item in shopping_list:
        print(item)


#Instructions
print("Add Items to your shopping list")
print("Type DONE if you're ready adding items")
print("TYPE HELP to show the different commands")

#Input
while True:
    new_item = raw_input("> ")

    if new_item == 'HELP':
        print("LIST OF COMMANDS")
        print("TYPE DONE if you're ready adding items")
        print("TYPE HELP to show the different commands")
        print("TYPE SHOW to show the items in your shopping list")

    if new_item == 'SHOW':
        printer()

    if new_item == 'DONE':
        break

    shopping_list.append(new_item)

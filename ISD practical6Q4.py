shoppingList = []
# create an empty list to hold our items
while True:
    item = input("Enter your item one by one: ")
    # ask for things for the list
    if not item:
        break
    else:
        shoppingList.append(item)
    # add the item to the items list
print(shoppingList)    
# show the current list of items

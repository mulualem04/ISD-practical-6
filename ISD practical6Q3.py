nums = [] # empty list
for x in [1,2,3]:
    for y in [3,1,4]:
        if x!=y: # if the value of x and y are not equal
            nums.append((x,y))
            # add the item to the items list  
            print(nums)
        else:
            print("They are equal,no append in the list")
            print(nums)

            
            
        
        

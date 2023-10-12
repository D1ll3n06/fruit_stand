# Dillen Dela Cruz
#11/3/2021

#function used to calculate index
def getIndex(fruitlist):
    get_index=input("Enter a fruit to see its index: ") #ask user to input fruit for index 
    if get_index in fruitlist: #searches for fruit in the list
        return fruitlist.index(get_index) # if input is in the list, the index will be displayed
    else:
        return None #returns if input is not in the list

#function used to search for the fruit after user's input
def search(intList):  
    search_fruit=input("Enter a fruit to search: ") #prompts user to input fruit for index
    if search_fruit in fruitList : #searches for value in the list
        return True # success if user's input is in the list
      
      
    else:
        return False # user's input is not in the list

#function used to remove user's input from the list 
def removeFruit(intList): 
    remove_fruit =input("Enter a fruit to remove: ") # prompts user to enter a fruit to remove 
    if remove_fruit in fruitList: #searches for existing fruit in the list 
        fruitList.remove(remove_fruit) #removes number if it's in the list 
        return True #removes number if it's in the list 
    else:
        return False #returns if user's input is not in the list 
    
    
#function used to add user's input from the list 
def addFruit(i): 
  if i == '6': #user inputs option 6
    add_fruit=input("Enter a fruit to add to the END of the list: ") #prompts user to input fruit to add 
    fruitList.append(add_fruit) #adds the fruits into the end of the list 
    return True
    
  elif i =='7': #user inputs option 7
    add_fruit=input("Enter a fruit to add to the BEGINNING of the list: ")#prompts user to input fruit to add         
    fruitList.insert(0,add_fruit) #adds the fruits into the beginning of the list 
    return True

#function used to sort the fruits list in different ways
def sortFruit (i):

# display first and last fruit in acending order
  if i == '8': #user inputs option 8
    fruitList.sort() #sorts list in ascending order 
    print ('The first and last fruit of the sorted list is ', end= '')
    print (fruitList[0],'and', fruitList[-1]) #displays first and last fruit in the list 
    
  
  
#descending
  if i == '9':#user inputs option 9
    fruitList.sort()  #sorts list in ascending order 
    fruitList.reverse() #sorts list in descending order 
    print ('The list has been sorted in descending order') #confirmation text 
    print()
    for item in fruitList: #prints out list 
        print(f'***{item: ^20}***')

  
#ascending
  if i == '10': #user inputs option 10
    fruitList.sort()  #sorts list in ascending order 
    print ('The list has been sorted in ascending order') #confirmation text 
    print()
    for item in fruitList: #prints out list
        print(f'***{item: ^20}***')

  
# display list A-M
  if i == '11': #user inputs option 11
    fruitList.sort() #sorts list in ascending order 
    i = 0 
    
    print ('The fruits have been sorted from A thru M')
    print()
    while i < len(fruitList): #loop used to get through the entire list 
      if fruitList[i].startswith(('A','B','C','D','E','F','G','H','I','J','K','L','M')) :
        print(f'***{fruitList[i]: ^20}***') #used to sort the list that meets the condition 
      i+=1 #used to move on to the next index


# display list N-Z
  if i == '12': #user inputs option 12
    fruitList.sort() #sorts list in ascending order 
    i = 0
    print ('The fruits have been sorted from N thru Z')
    print()
    while i < len(fruitList): #loop used to get through the entire list 
      if fruitList[i].startswith(('N','O','P','Q','R','S','T','U','V','W','X','Y','Z')) : 
        print(f'***{fruitList[i]: ^20}***') #used to sort the list that meets the condition 
      i+=1 #used to move on to the next index





# Startup Banner
print()
print('----------------------------------')
print('Welcome to the Fruit List program')
print('----------------------------------')



#initialization of the list 
fruitList = ['Oranges', 'Apples', 'Grapes', 'Bananas', 'Pears', 'Grapefruit', 
             'Lemons', 'Pineapples', 'Peaches', 'Apricots']

#Priming the loop to begin
Continue ='Y'

# Loop initialized and program starts
while Continue == 'Y': #continue, if the user input's Y
    
#menu displayed
    print("\nSelect an option: ") #prompts user to select an option from the menu 
    print("1. Display the fruits in the list\n2. Display how many fruits are in the list"
        "\n3. Get the index number of a fruit\n4. Search for a fruit\n5. Remove a fruit from the list"
        "\n6. Add a fruit to the END of the list \n7. Add a fruit to the BEGINNING of the list"
        "\n8. Display the first and last fruit in the sorted (ascending order) list \n9. Sort the fruits list in descending order"
        "\n10. Sort the fruits list in ascending order \n11. Display the fruit in a sorted (ascending order) list A thru M"
        "\n12. Display the fruit in a sorted (ascending order) list N thru Z."
        "\n13. Copy the list into a new list\n14. Exit the menu") #the menu list the user choose from 
    
    #  users selection entered  
    option=input("\nOption: ")
    
    #program action based on user selection
    
    if option=='1': #user inputs 1
        print()
        print('  All items in the list:') 
        for item in fruitList: #prints the fruit list 
            print(f'***{item: ^20}***', end=' ')
            print()
            
    elif option=='2':#user inputs 2
        print()
        print(f'There are {len(fruitList)} fruits in the list') #prints the number of fruits in list
        
        
    elif option=='3': #user inputs 3
        index= getIndex(fruitList) #gets index from function
        if index is not None:  #searches for index if user's input is in the list
            print()    
            print("Fruit is found at index: ", index) #displays index
        else:
            print()
            print("Fruit is not in the list.") #if user inputs a fruit not in the list
            
    elif option=='4': #user inputs 4
        if search(option): #searches for fruit in the list after user's input using search
            print()    
            print("Fruit exists in the list.") #user's fruit is in the list
        else:
            print()
            print("Fruit does not exist in the list.") #user's fruit is not in the list 
    
    elif option=='5': #user inputs option 5
        if removeFruit(fruitList): #removes fruit from the list
            print()
            print("Fruit removed from list.")
            print()
            for item in fruitList: #displays updated list with removed item 
                print(f'***{item: ^20}***')
        

        else: #fruit is already not on the list
            print()    
            print("Number is not on the list.")
    
        print()
        
    elif option == '6': #user inputs 6
        addFruit(option) #user's input is added to the end of the list 
        print()
        print('The fruit was added to the END of the list')
        print()
        for item in fruitList: #displays the updated list with new fruit
            print(f'***{item: ^20}***')
  

    elif option == '7': #user inputs 7
        addFruit(option) #user's input is added to the end of the list
        print()
        print('The fruit was added to the BEGINNING of the list')
        print()
        for item in fruitList: #displays the updated list with new fruit
            print(f'***{item: ^20}***')
    
    elif option == '8': #user inputs 8
        sortFruit(option) #displays first and last fruit in the sorted list 

    elif option == '9': #user inputs 9
        sortFruit(option) #displays the list in descending order 

    elif option == '10': #user inputs 10
        sortFruit(option) #displays the list in ascending order 
        
    elif option == '11': #user inputs 11
        sortFruit(option) #displays the fruit in a sorted list A thru M

    elif option == '12': #user inputs 12
       sortFruit(option) #displays the fruit in a sorted list N thru Z
     
    elif option == '13': #user inputs 13
        i = input ('what name would you like to name your list? ') #prompts user to name the copy list
        print()

        copy_list= fruitList.copy() #copies the list 
        print("All items in the original list: ") #displays the original list 
        for item in fruitList:
            print(f'***{item: ^20}***')
        print()


        print(f'\nAll items in the {i} list: ') #displays the copied list and the name of the user's list
        for item in fruitList:
            print(f'***{item: ^20}***')


    elif option=='14': #user inputs 14
        print()    
        print("Thank you for using the fruit List program")
        Continue ='N' #exits the program

   
    else: #user enters input that is not on the menu
       print()    
       print("Invalid Selection.")





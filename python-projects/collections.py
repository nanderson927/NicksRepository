#Lists
lst = [10,20,30,40,50]
lst.append(5) #adds elements
lst.append(6)
lst.append(7)
print(lst)

lst.remove(40) #removes 40 from list
print(lst)
lst.pop(2) #removes element at index 2
print(lst)

lst.reverse() #reverses list, modifies the list
print(lst)

lst.sort() #sorts list in ascending order
print(lst) 

lst[0]=500 #makes element at index 0 equal to 500
print(lst)

#slicing lists, similar to strings
lst=lst[1:] #slices first element from list
print(lst)

index10 = lst.index(10) #gives index of element '10'
print(index10)

lst.append(20)
lst.append(20)
lst.append(20)
print(lst)
count20 = lst.count(20) #counts number of times 20 occurs
print(count20)

copy_lst = lst #makes a copy of list with same mem address as lst
print(copy_lst)
copy_lst[0]=99 #alters both copy_lst and lst, be careful
print(copy_lst)
print(lst)

new_copy = lst.copy() #makes copy of lst with diff mem address than lst
new_copy[0]=500 #alters only new_copy and not lst
print(new_copy)
print(lst)

new_copy=lst[:] #also creates copy of list with diff mem address

empty_lst = [] #creates empty list
for val in lst: #adds all values from lst to empty_lst
    empty_lst.append(val)
print(empty_lst)

empty_lst=[0]*10 #new list with 10 zeroes to begin
print(empty_lst)
#must use append to add values outside list range

squares = []
for i in range(1,10): #fills list with squares of numbers 1-9
    squares.append(i*i) #i**2 is i squared
print(squares)

#List comprehensions: another way to create a list using existing sequence
squares = [x*x for x in range(1, 10)] #creates same squares list as above
print(squares)

plus_5 = [x+5 for x in lst] #creates list that is each element in lst plus 5
print(plus_5)

#filter values using list comprehension
small_values = [x for x in lst if x<20] #creates new list with all numbers less than 20 in lst
print(small_values)

#Dictionaries: Collection that stores key and value pairs
fav_foods = {"Kathleen" : "pizza", "Hannah":"pasta", "Kush":"Fries", "Yamill":"Fries" }  
#separate keys and entries with colons, separate entries with commas
#keys must be unique
print(fav_foods)
hff = fav_foods["Hannah"] #assigns hannah's fav food to 'hff'
print(hff)

for key in fav_foods: #prints a sentence that states each person's fav food
    print(f"{key}'s favorite food is {fav_foods[key]}") #f allows us to embed variables in strings

for person, food in fav_foods.items(): #another way to print each person's fav food
    print(f"{person}'s favorite food is {food}")

#bff = fav_foods["Bob"] results in key error
if "Bob" in fav_foods: 
    print(fav_foods["Bob"])
else: #adds bob to dictionary
    fav_foods["Bob"] = "wings"
print(fav_foods)

if "Bob" not in fav_foods: #adds bob if he is not in dictionary
    fav_foods["Bob"] = "wings"



















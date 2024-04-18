num = int(input("Enter a number: ")) #int() makes sure input is treated as an integer so we can modify it
print(num) #otherwise it is treated as a string
num+=10
print(num)

try: #code here is tried, if it throws an error, except block is executed
    num = int(input("Enter a number: ")) 
    num += 10
    print(num)
except:
    print("You did not enter a number")

print("continue")

with open("movies.txt") as file: #this reads file in
    for line in file: #prints each line in the file
        line = line.strip() #gets rid of new line at the end of the string variable 'line'
        print(line)

with open("heights.txt") as file:
    for line in file:
        line = line.strip()
        lst = line.split() #split function splits each line by word
        print(lst) #returns a separated list 




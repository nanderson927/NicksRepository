print("hello, world!")

#this is a comment

#Loops
#for loop
nums = [10, 20, 30, 40, 50]
for i in range(len(nums)):
    print(nums[i])

#for each loop
for num in nums: #"num" can have any variable name
    num += 5 #modifies num within array only in loop
    print(num)
print(nums)
#enumerate
for i, val in enumerate(nums):
    print("i is", i, "and val is", val) #concatenate with comma

#practice
people = ["Nick", "Paul", "Troy", "Katie"]
for val in people:
    print(val)
for i in range(len(people)):
    print(people[i])
for j, var in enumerate(people):
    print(var)

#getting sum of numbers in array
ans = [2, 4, 6, 8, 10]
sum = 0
for num in ans:
    sum += num
print(sum)
print(f"the sum of ans is {sum}") #alternative print statement

#Functions
def hello(name="friend"): #defines function with default value of friend
    print("hello!",name) #name is a parameter
hello() #calls function with no parameter, gives default value
hello("Bob") #calls function with parameter

#Strings
fname = 'Nick'
lname = "Anderson" #can use single or double quotes, good if there are apostroohes
#print('She's a great dancer) - error, use double quotes

#concatenation
    #can use + operator
full_name = fname + lname
print(full_name)

#characters within strings
first_char=fname[0]
print(first_char)
#negative index places get that many spaces from the end
#in "python", -1  is n, -2 is o...

#length
print(len(fname))

#repetition operator
name_3=fname*3
print(name_3) #prints anme 3 times

#comparing strings
#no need for .equals
#can use == operator with strings
if fname =="Nick":
    print("nice")

#upper method 
fname_uppercase = fname.upper()
print(fname_uppercase) #prints name in all caps

#slicing strings
#method: String[start index:end index], up to but not including end index
platform_computing = "Platform Computing"
platform = platform_computing[0:8]#starting index defaults at 0
computing = platform_computing[9:18]#ending index defaults at end of string
print(platform, computing)

#Arrays
nums = [0, 3, 8, 5, 4]
#swap 8 and 4
temp = nums[2]
nums[2]=nums[4]
nums[4]=temp

print(nums)


    





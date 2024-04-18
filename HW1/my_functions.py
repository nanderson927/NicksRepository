#Nick Anderson


def even(nums):
    """
    This function takes a list as a parameter and returns 
    the number of even numbers of the list
    """
    sum = 0
    for val in nums:
        if val%2==0:
            sum+=1
    return sum


def e_finder(string, num):
    """
    This function counts the number of times the letter 'e' 
    occurs in any string after any starting index
    """
    num_e=0
    sliced=string[num:]
    for letter in sliced:
        if letter=='e':
            num_e+=1
    return num_e


#test even function
print('The number of even numbers is', even([1, 2, 3, 4, 5, 6]))
print('the number of even numbers is', even([22, 24, 10, 13, 45, 1000]))
print('The number of even numbers is', even([1, 3, 5, 7, 9,]))

#test e_finder function
print("The number of e's is", e_finder('aaaeeeiiioouuueeee', 4))
print("The number of e's is", e_finder('eegggghhhhjjje', 4))
print("The number of e's is", e_finder('eeeeiiiddddlll', 5))
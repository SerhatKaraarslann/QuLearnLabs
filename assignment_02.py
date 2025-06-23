"""This function takes a list of integers and return the average of list elements, that are divided by 2.
@param input: list of integers
@type input: list[int]
@return: average of list elements, that are divided by 2
@rtype: float
@author: Serhat Karaarslan
"""
def avg_two(input:list[int]) -> float:
    
    #List for the numbers that are divided by 2
    list1 : list[int] = []

    #Loop through the input list 
    for i in input:
        #check if the element of input list is divided by 2
        if i%2 == 0:
            #if it is , append it to the list1 which is created for the numbers that are divided by 2 in the input list
            list1.append(i)

    ##return the sum/len of the list1 which is the average of the numbers that are divide by 2.        
    return sum(list1)/len(list1)

numbers = [1, 6, 10, 15, 99, 45, 56, 32, 150, 151, 672, 558, 789, 335, 23, 65, 47, 33]
print(avg_two(numbers))

inp : list[int] = [2,8,15]
ouput = avg_two(inp)
print(ouput)

# In this version, I use the same logic as the first one, but I use list comprehension
def avg_two2(input : list[int]) -> float:
    #same logic as the first but shorter with list comprehension
    list1 : list[int] = [i for i in input if i%2 == 0]
    return sum(list1)/len(list1)


numbers = [1, 6, 10, 15, 99, 45, 56, 32, 150, 151, 672, 558, 789, 335, 23, 65, 47, 33]
print(avg_two2(numbers))

inp : list[int] = [2,8,15]
ouput = avg_two2(inp)
print(ouput)


#in this version, I use the same logic but I don't use any list to store the numbers which are divided by 2.
#I just use a sum and count variable to calculate the average of the numbers that are divided by 2.
def avg_two3(input :list[int]) -> float:

    #int variables to store sum of the numbers which are divided by 2
    sum : int = 0
    #int variable to store the count of this numbers
    count : int = 0

    #loop iteate through the input list
    for i in input:
        #check if the element of input list is divided by 2
        if i%2 == 0:
            #if it is, add it to the sum and increase the count by 1
            sum += i
            count += 1
    
    return sum/count


numbers = [1, 6, 10, 15, 99, 45, 56, 32, 150, 151, 672, 558, 789, 335, 23, 65, 47, 33]
print(avg_two3(numbers))

inp : list[int] = [2,8,15]
ouput = avg_two3(inp)
print(ouput)
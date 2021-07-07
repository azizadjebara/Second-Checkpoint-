#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Write a program that will find 
# all numbers which are divisible by 
# 7 but are not a multiple of 5, between 
# 2000 and 3200 (both included). The numbers obtained should be printed in a list.


# In[17]:


def ex1() :
    list_valid_number = []
    for i in  range(2000 ,  3200) : 
        if (i%7 == 0 and i%5 !=0 ) :
            list_valid_number.append(i)
    return list_valid_number


# In[ ]:


# Write a program that can compute the factorial of a given number. 
# (the factorial of n is the product of all positive integers less than or equal to n). 
# for example factorial(5)= 5 x 4 x 3 x 2 x 1 the result is 120.  (i.e. factorial (0)=1) 


# In[28]:


def ex2(nmbr) :
    result = 1 
    for i in range( 1, nmbr + 1 ) :
        result = result * i
    return result

ex2(5)


# In[29]:


# With a given integer number n, 
# write a program to generate a dictionary 
# that contains (i, i*i) such that is an integral
# number between 1 and n (both included). and then the program should print the dictionary. 
# Suppose the following input is supplied to the program: 8 Then, the output should 
#     be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}  


# In[50]:


def ex3(nmbr):
    result = { i : i * i for i in range(1 , nmbr + 1) }
    return result
    
ex3(8)


# In[74]:


# Given a non-empty string and an int n, return a new string where the char at index n has been removed. 
# The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive). 

# missing_char('kitten', 1) → 'ktten'    for example here we remove "i" which is located in the index 1

# missing_char('kitten', 0) → 'itten'   here we remove "k" which is in the index 0

# missing_char('kitten', 4) → 'kittn'   here we remove "e" which is in the index 4

test = 'test' 

def ex4(text , indx):
    return text[:indx] + text[indx+1:]

ex4('salutt' , 5 )


# In[118]:


# Write a NumPy program to convert a NumPy array into a Python list structure.
# Expected Output: 
# Original array elements: [[0 1] [2 3] [4 5]] 
# Array to list: [[0, 1], [2, 3], [4, 5]] 

[0,1,2,3,4,5,6,7,8]

import numpy as np

def ex5(nmbr): 
    if(nmbr % 2 == 0) :
        print('Original array elements : ')
        result = np.arange(nmbr).reshape(nmbr//2 , 2)
        print(result)
        print('Array to list : ')
        return result.tolist()
    else : 
        print('Original array elements : ')
        result = np.arange(nmbr - 1).reshape(nmbr//2 , 2)
        print(result)
        print('Array to list : ')
        newres =  result.tolist()
        newres.append([nmbr])
        return newres

ex5(6)


# In[136]:


# Write a NumPy program to compute the covariance matrix of two given arrays. 

# Original array1: [0 1 2] 

# Original array2: [2 1 0] 

# Covariance matrix of the said arrays: [[ 1. -1.] [-1. 1.]]
 
# Hint: We can use the np.cov() function to calculate the covariance between these two arrays
 
import numpy as np

array1= [0 ,1,2]
array2= [2,1 ,0]

def ex6(arr1 , arr2) :
    covariance=np.cov(arr1 , arr2)
    return covariance.tolist()

ex6(array1 , array2)


# In[151]:


import math
# Question: Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H] 

# The following are the fixed values of C and H: C is 50. H is 30. 

# D is the variable whose values should be input into your program in a comma-separated sequence. (that means D contains more than value)

# Example Let's assume the following comma-separated input sequence is given to the program: 100,150,180 The output of the program should be: 18,22,24 

# To further explain this, we will obtain a result for 
# each value of D:  Q1= Square root of [(2 * C * 100)/H] =18, Q2= Square root of [(2 * C * 150)/H] = 22 and Q3 = Square root of [(2 * C * 180)/H]  = 24

# Hints: If the output received is in decimal form, it should be rounded off to its nearest value 
#     (for example, if the output received is 26.0, it should be printed as 26) In case of input data being supplied to the question, 
#     it should be assumed to be a console input. 
D = [100,150,180] 

def ex7(arrNum):
    C = 50 
    H = 30
    results = []
    for i in arrNum : 
        Q = math.sqrt((2 * C * i)/H)
        results.append(int(round(Q , 0)))
    return results 

ex7(D)


# In[ ]:





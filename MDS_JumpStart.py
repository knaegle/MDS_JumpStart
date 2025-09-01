#!/usr/bin/env python
# coding: utf-8

# Modifed from *Introduction to Programming in the Biological Sciences Bootcamp* © 2023 Justin Bois (Caltec).
# Check out the original notebook <a href="https://justinbois.github.io/bootcamp/2023/index.html">here</a>

# ## Homework Jump Start: Quick Introduction to Data Science using Python

# ### Introduction

#  The goal of this homework is to help you get setup with the nevironment you'll be using to code. This is a hands-on class that will require a proficient grasp of programming. We'll be using python exclusively for this class. There are many options for where you will code and your environments. For example, <a href="https://colab.research.google.com/">Google Colab</a>, JupyterLab which you can get through <a href="https://www.anaconda.com/products/navigator">Anaconda Navigator</a>, or an Integrated Development Environment like <a href="https://code.visualstudio.com/download">Visual Studio Code</a>. 
# 
# Once you have downloaded, installed and setup your coding environment, the next step is importing the necessary packages. Google colab and JupyterLabs should have these packages already installed and all you need to do is import them to access their functionalities. When using an IDE, we highly recommend you setup an environment specifically for this class (for example: <a href="https://code.visualstudio.com/docs/python/environments">Visual Studio Python Environments</a>). Base python provides all you need to write complex programs for any task you need, but, you don't really want to have to write your own code for everything. Luckily, there are many packages that you can install on top of base python that you can use to make your life easier and quicker (see the table in the UVA Computational Resources repo for examples of commonly used packages at UVA).
# 
# The following lines of code allows you to import NumPy, SciPy, Matplotlib, and Pandas, which you'll be using for this homework. Coding convention stipulates that you import your packages at thr top of your script, and with the aliases used below. 
# 
# To learn more about packages and modules, click <a href="https://justinbois.github.io/bootcamp/2023/lessons/l10_packages_and_modules.html">here</a>. 

# In[ ]:


import os # this package provides a way of using operating system dependent functionality like reading or writing to the file system
import pandas as pd #you can refer to pandas as pd now, so pd.DataFrame - this package handles data manipulation and analysis
import numpy as np # this package contains important numerical handling functions
from scipy import stats # this package is used for scientific and technical computing -- this is an example of importing just one part of a larger package.
import matplotlib.pyplot as plt # this package is used for creating static, animated, and interactive visualizations in Python. 
import seaborn as sns # this package is also a data visualization package. 


# ### Section 1: Conditionals

# Write an if-else statement that prints "A is greater than B", when the numeric value of A is greater than B, and prints "A is less then B", when the numeric value of A is less than B. Show that your code works

# In[ ]:





# Using "if", "elif", and "else", write a statement that prints:
# "Inside the If" - when the boolean expression inside of the if statement is fulfilled; 
# 
# "Inside the elif" - when the boolean inside of the elif statement is fulfilled;  and finally
# 
# "inside the else"-  when neither are fulfilled. Show that your code works. 

# In[ ]:





# ### Section 2: Loops

# Use a for loop to print every value in the my_list variable shown below; 
# 
# Next, append the number 15 to the list and print the entire list as a whole (different from printing the contents individual).

# In[ ]:


my_list = [1, 2, 3, 4, 5]


# Use a while loop to print only the first three values of "my_list" above

# In[ ]:





# Using a while loop, write a program to keep asking for a number until you enter a negative number. Once a negative number is entered, print "the negative number entered is" negative_number.

# In[ ]:





# ### Section 3: Functions

# Write a function that requests the _height_ and _radius_ of a cylinder and then calculates the _volume_ and _surface area_ of the cylinder. 

# In[ ]:


def calculate_cylinder_volume(height, radius):
    # put your code here
    return volume, surface_area


# In[ ]:


# demonstrate your code here
volume, surface_area =calculate_cylinder_volume(10, 5)
print("Volume:", volume)
print("Surface Area:", surface_area)

# do some checks here on your code -- you can assert a specific return given a set of inputs, you can also compare the volume between two cylinders
# and check that the surface area and the volume scale as expected between the two cylinders


# Your turn without a template: Write a function that requests a number of elements, and returns a list of element size filled with randomly generated integers from 0-99. For example, if I input 3, the function could return [5,19,20].  

# In[ ]:





# ### Section 4: Dataframe Manipulation

# Import the "country_vaccinations.csv" file as a pandas dataframe. How many rows and columns are in this dataframe? Use df.info() to display information on all columns of the data. 

# In[ ]:





# Using a for loop, Calculate and print the sum, mean and standard deviation for every float column in this dataframe

# In[ ]:





# ### Section 5: Plotting

# Make a plot showing the total vaccinations per hundred for the United States, Canada, Mexico, Cuba, Jamaica, Dominican Rebublic and Haiti. 

# In[ ]:





# Bonus: Make any additional plots that supplement your understanding of the dataset. What interpretations can you make from your plot?

# In[ ]:





# In[ ]:





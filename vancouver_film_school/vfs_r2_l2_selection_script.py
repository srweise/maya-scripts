import maya.cmds as cmds #Imports Maya API

selection = cmds.ls(selection=True) # stores selection in a variable
# If you use a list comprehension you can fit everything into 2 lines of code instead of 5 and its more pythonic.
# Example:
# my_list = [i for i in selection if "end" not in i]
# cmds.select(my_list)

my_list = [] # creates an empty list

for obj in selection: # Goes through objects in selection
    if "end" not in obj: # check if string is in the name of the object
        my_list.append(obj) # if it's not, add it to the previously created list
        
cmds.select(my_list) # select elements part of the list

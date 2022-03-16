# crispy-carnival
Converting JSON to CSV

Develop a python script that processes a json file and converts it to a csv file that could be opened in Microsoft Excel. We've covered most of the content for handling csv and json files in modules 6 & 7. However, this module is focused on not only the syntax of building a script but how to go about it in a way that produces more elegant code.

Objectives:
This assignment will give you the opportunity to:

Demonstrate ability to convert a file format from one common format (json) to another (csv)
Become comfortable using the csv library available in python
Use key information in a dictionary
Use code minimalism in developing a python script

Guidelines:
Try to have running code as much as possible by:

Using the debugger when you need to check the value of certain variables

Shifting between editing in vim and running of the script (the debugging two-step)

Fixing an error as soon as you run into it

Do not write your code like you write a term paper

Proper functions will mean that your code is not run sequentially

Following the principles of code minimalism

See the video on code minimalism for more details

Instructions:
To complete this assignment follow these steps:

Download the 2015 VA Mental Health data   Download 2015 VA Mental Health data (retrieved from data.gov)
Create a script called va_mental_health.py to process the file
In your script load the VA Mental Health data using the json libraries
Use a for loop to move through each dictionary in the VA Mental Health Data
Use the csv libaries to convert the data to csv format and write the data to an output file named output.csv (each dictionary is converted to a single csv formatted line) with the following alterations:
If the ValueType is a percentage then convert the value to a floating point with two decimals of accuracy then convert back to a string (Example: 62% should be converted to .62)
If the ValueType is a number then remove commas from the outputted number (Example: 13,493 should be converted to 13493)
Make sure that your csv file has a header row with each header name corresponding to the key value in the json dictionaries.
Code minimalism requirements:
You should use the if __name__=='__main__':  syntax to call your main method
Your code should include at least three functions (including the main function)
Do not use global variables. If a function needs a variable then pass it as a parameter.
The only code at the far left indent should be functions, import statements, and the if statement that calls the main function
Do not use inner functions (a function within a function)
Open your output.csv file in Microsoft Excel to make sure that the data came across correctly.
Submit your python file to complete the assignment

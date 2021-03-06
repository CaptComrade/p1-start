import matplotlib.pyplot as plt
import numpy as np
import sys

filename = sys.argv[1]        # Stores ARG1 in filename, as in: $ python plot.py ARG1 ARG2 

# This bit of code creates a dynamic skiprows value
# Needed because the pre-data info on some cut up data files don't have equal amounts of non-data rows
datafile=open(sys.argv[1], "rt")
count=0
while datafile.readline()[0] is '"':
	count += 1
# Creates array of arrays
# Each array is the stress and strain values for each measurement
data = np.loadtxt(filename, delimiter=",", skiprows=count, usecols=(3,7))   # Attempts to load filename into local variable data.

# Separates y_data (stress) and x_data (strain)
# Then adjusts data so that stress starts at 0, and both stress and strain go up and not down
y_data=data[:,0]
x_data=data[:,1]
y_data_adjust=(y_data*-1)-(y_data[1]*-1)
x_data_adjust=x_data*-1

## Part 0
# Figure out what arguments to add to the loadtxt function call
# so that numbers are loaded into the local function 'data'.
# Hint: look for arguments like 'skiprows' and 'delimiter'
# Check by running:
#   $ python plot.py raw-data/Sp15_245L_sect-001_group-1_glass.raw
# at the command line.


## Part 1
# Figure out what columns and rows of data we need to plot
# Stress (y-axis) vs Strain (x-axis)
# plot raw-data/Sp15_245L_sect-001_group-1_glass.raw
# Make sure to include axis labels and units!


#Uses numpy to automatically find linear regression
#Plots the stress vs strain, as well as the linear regression
#Stores the resultant figure in a filename of the last character before the .raw
regSlope, regIntercept = np.polyfit(x_data_adjust,y_data_adjust, 1)
f_linear = np.poly1d((regSlope,regIntercept))
print("Young's Modulus is " + str(regSlope) + " MPa")
plt.plot(x_data_adjust,y_data_adjust,color='k',linestyle='-')
plt.plot(x_data_adjust,f_linear(x_data_adjust),color='#2929a3',linestyle='--',label='Linear Regression')
plt.xlabel('Strain [% Extension]')
plt.ylabel('Stress [MPa]')
plt.legend(loc='best')
plt.show()
path = str(filename[-5])+'.png'
plt.savefig('graphs/'+path)


## Part 2
# Check to see if your code in part 1 will plot all of the files in raw-data/
# Edit the files (use git liberally here!) to make them more usable


## Part 3
# Use linear regression to calculate the slope of the linear part of
# the stress-strain data. Plot your line against the data to make 
# sure it makes sense! Use the slope of this line to calculate and print
# the Young's modulus (with units!)

## Part 4
# Modify your code to save your plots to a file and see if you can generate
# plots and Young's moduli for all of the cleaned up files in your data 
# directory. If you haven't already, this is a good time to add text to 
# your .gitignore file so you're not committing the figures to your repository.




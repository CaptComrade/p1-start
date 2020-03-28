DEPENDENCIES
------------
Numpy
Pyplot
Sys

HOW TO GET
----------
Import numpy as np, sys, and matplotlib.pyplot as plt

HOW TO RUN
----------
1. Ensure that you are able to import the required dependencies.
2. Data files must be of a single test; they must end with numbers, and multiple test files must be cut up into separate files.
3. Make sure that each of your data files has a unique character before the ".raw"; the way the program is set up, that last character is used to store the figure printed.
4. After navigating to the directory containing the plot.py file, as well as the raw-data/ and graphs/ directories, the former of which will contain the data, type this and hit enter in a terminal: python plot.py raw-data/[filename]
5. You will be given a graph after the computations are done. The figure is stored as a png in graphs/.

EXAMPLE RUN
-----------
python plot.py raw-data/Sp_15_245L_sec-001_group-01_bendtest-aluminum_3.raw

Will show a plot for a single test for aluminum, and store a figure named 3.png in graphs/

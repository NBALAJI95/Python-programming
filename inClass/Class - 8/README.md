This is a python program for generating baby names (boys and girls) using Hidden Markove Model
(HMM). There are 2 text files "namesBoys.txt and namesGirls.txt that contain names for boys
and girls. The program uses these 2 text files to find patterns and generate new names based on
the length of the name that is entered by the user.
From command line: full name is generated.
You can also get full name without specifying gender.
The random name picker relies on the cumulative frequencies which is in the included Census data files. 
A random float is chosen between 0.0 and 90.0, Name file lines are iterated through until a cumulative frequency is found that is less than the randomly generated number and then, the name on that line is chosen and returned (or printed out).

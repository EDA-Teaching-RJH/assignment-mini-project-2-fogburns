
- sys_check(): Used sys.argv to check version of python being used, if under 3.8 it exits the function as python 3.8 is required. At first i had to print the whole sys.version_info to see how the data was being stored, after this i was able to identify the numbers used to log the version data to then call directly and create variables to then use them.(Workshop 7 + Lecture 9)

- get_yn(): Used in other functions when a yes or no answer is required, simplifies rest of code and makes it easier to read.

- auto_fill(): Used mostly for testing or if the user doesnt want to manually input details, uses random to generate a random dictionary of data to return to the user. Began trying to return them as variables straight away but became complicated and errors occurred, using a dictionary simplified this process, although I had to return them back as variables to calculate.(Lecture 7)

- initial_q(): Used as a confirmation before the script begins, includes cowsay to make beggining look more interesting.(Workshop 7)

- name_q(): Used to get name from user, only allows normal characters, using re as a filter to easily accept or reject this.(Workshop 8)

- height_q() Introduces map to 'ft' and 'inch', to set them both as integers.

- colour_q(): Used re to filter only characters from input by user.(workshop 8)

- erate_q(): Used isinstance to check if 'erate' and 'rate' is float or integers and prints dependant on that.

- save_r(): Used to save results to a downloadable file, first tried with csv but became complicated trying to print in certain ways, found that json was easier to format my data and looked cleaner code wise. With this can also see last completed survey.(Lecture 8, Lecture 7)

- line(): Simplify rest of code and make it easier to read.

- line(423)survey.py: Uses an if statement to tell whether the code is being imported. If it is it wont run, This will stop any errors if the script is imported.(Workshop/Lecture 7)

- line(14)calc.py: similar to the above it will only run if the file is being imported as its not suppose to be ran directly(Workshop/Lecture 7)

- calc.py: Used to simplify main() function aswell as making it easier to read, computed all data in seperate file, returns processed data, including dates of estimated death so the main() function can print easily, had difficulty printing the date correctly (only wanted to print as YY/MM/DD, I wanted the reversed order), so I had to assign a variable to each value of the date then print as I want. Used class to group these functions together, self.rng to create reproducable results if seed is provided in main script, used for testing to give same results each time to simplify things. Uses random to create different results each time. (workshop 7,Lecture 9, Lecture 7)

- class Timetype: Tells script what data types variables are to ensure data is carried corrcetly (Lecture 9)

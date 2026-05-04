Write down:
- What is the problem?

Suppose you have n numbers of line of log file

And you have to extract the meaningful information out of it

Read each line can leads human error, unnesscary time consumption

- What input does it need?

Initial when we started writing i was giving a log file as an input to code during runtime

Now using argparse we can pass file and desired output files name as arugment 

- What output should it give?

After reading, analyzing, making changes return a output.json file

- What steps are involved?

main code is break in 

first read the log file which will return output as list [data]

second create an empty dict to store the key,values with initial value 0

third 

using for loop iterate the lines of list we got from the first step

check the key word in each line, if word in list present then add +1 in value of dict

similarly goes with other key, values

fourth return log count file with the updated values

fifth using the return log count value, write it as json file 

optional create class of all function for modularity, resuablity

use argparse pass the log file and output file name in command




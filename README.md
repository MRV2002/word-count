# word-count
There are many methods to count word or given string, here i mention few of them with a proper code.
Quick Ninja Methods: One line Code to find count words in a sentence with Static and Dynamic Inputs.
Method : Using split() split function is quite useful and usually quite generic method to get words out of the list, but this approach fails once we introduce special characters in the list.
Method  : Using regex(findall()) Regular expressions have to be used in case we require to handle the cases of punctuation marks or special characters in the string. This is the most elegant way in which this task can be performed.
Method : Using sum() + strip() + split() This method performs this particular task without using regex. In this method we first check all the words consisting of all the alphabets, if so they are added to sum and then returned.
Method : Using operator.countOf() method

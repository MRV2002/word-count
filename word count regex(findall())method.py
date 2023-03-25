import re
 
# initializing string
test_string = "I am vickram"
 
# printing original string
print ("The original string is : " + test_string)
 
# using regex (findall())
# to count words in string
res = len(re.findall(r'\w+', test_string))
 
# printing result
print ("The number of words in string are : " + str(res))
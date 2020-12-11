### hw1 - part 3

# Earlier this week, you learned to think about data processing and how to perform
# basic string and list operations. In this assignment, you'll count the lines,
# characters, and words in a file.

# We will keep things simple and define a word as something that is delimited by
# any whitespace, so that the number of words on a line that is read from a file
# is simply the number of strings returned by split().

# To help you get started on this first programming assignment, here is a list
# of Python functions and methods that we've discussed (or will discuss) in
# class, or covered in supplement 2, that you may find useful:
#    raw_input (optional)
#    open
#    split
#    len
#    print
#    rstrip()


print("----------")

# Try to make your program work first on test.txt, which has 22 characters,
# 3 lines, and 5 words.
# (Note: you should include end of line characters in this character count!) 
#
# Then look at the contents of hw1feed.txt, so you can get a
# sense of the right answers, approximately. It's data extracted from our class
# Slack workspace -- just the top-level posts in the #general channel.
#
# Run your program on hw1feed.txt and sherlock.txt.

fname = "test.txt"
#fname = input("Please enter a file name: ")
numChars = 0
numLines = 0
numWords = 0

# fill in your code here


# output code below is provided for you; you should not edit this
print('%d characters'%numChars)
print('%d lines'%numLines)
print('%d words'%numWords)

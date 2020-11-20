"""
The program is trying to translate a sentence captured as user input
We first read in the text file textese.txt.
Then from the text file, we create a list of strings from each lines in the text file.
Then, we create a dictionary on the list
Once the test file has been read into the memory, we close the file.

We then define a function for translating which envolves splitting the user input (sentence) into an
array of strings ("enjoy the excellent band tonight") ["enjoy", "the", "excellent", "band", "tonight"]

Once we have the array of strings representing the user's input sentence, we 
loop through each words, find the key matching the word and returns back the value tied to the word in our dictionary.

After each word is translated, we then 
print out the translated sentence to the user. 

"""
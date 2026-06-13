#import emoji library to convert emoji codes into emoji
import emoji

#ask user for text input
text = input("input: ")

#Convert emoji codes and aliases into emojis, then print result
print("Output: " ,emoji.emojize(text , language = "alias" ))


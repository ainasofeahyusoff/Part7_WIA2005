# Load a dictionary or word list containing valid words
dictionary = ["That", "Person", "Has", "Motive"]

# Function to unscramble a word using the Anagram Approach
def unscramble_word(word):
    sorted_word = sorted(word)
    unscrambled_words = []
    
    for dict_word in dictionary:
        sorted_dict_word = sorted(dict_word)
        if sorted_dict_word == sorted_word:
            unscrambled_words.append(dict_word)
    
    return unscrambled_words

# Accept jumbled words from the user
num_words = int(input("Enter the number of jumbled words: "))
jumbled_words = []
for i in range(1, num_words + 1):
    jumbled_word = input("Enter jumbled word #{}: ".format(i))
    jumbled_words.append(jumbled_word)

# Unscramble the words and display the results
print("Unscrambled message:")
for word in jumbled_words:
    unscrambled = unscramble_word(word)
    print("{}: {}".format(word, ", ".join(unscrambled)))
def find_longest_word(text):
    # Split the text into words
    words = text.split()
    
    # Find the length of the longest word
    longest_length = max(len(word) for word in words)
    
    # Find all words that have the longest length
    longest_words = [word for word in words if len(word) == longest_length]
    
    return longest_words

# Example usage:
text = "The quick brown fox jumped over the lazy dog"
longest_words = find_longest_word(text)
print("Longest word(s):", longest_words)

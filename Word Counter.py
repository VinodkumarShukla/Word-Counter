def count_words(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Count the number of words
    num_words = len(words)

    return num_words


# Example usage:
input_sentence = input("Enter a sentence: ")

# Count the number of words
word_count = count_words(input_sentence)

# Display the result
print(f"The number of words in the sentence is: {word_count}")
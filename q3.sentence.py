def max_words_in_sentence(sentences):
    max_words = 0
    for sentence in sentences:
        words = sentence.split() 
        max_words = max(max_words, len(words))  
    return max_words

sentences = ["This is a sample sentence", "Another sentence with more words", "Short sentence"]
max_words = max_words_in_sentence(sentences)
print("Maximum number of words found in a single sentence:", max_words)

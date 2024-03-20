def remove_common_words(s1, s2):
  
    words_s1 = s1.split()
    words_s2 = s2.split()

    set_s1 = set(words_s1)
    set_s2 = set(words_s2)

    common_words = set_s1.intersection(set_s2)
    

    filtered_s1 = [word for word in words_s1 if word not in common_words]
    filtered_s2 = [word for word in words_s2 if word not in common_words]
    

    result_s1 = ' '.join(filtered_s1)
    result_s2 = ' '.join(filtered_s2)
    
    return result_s1, result_s2


s1 = "This is a sample sentence"
s2 = "Another sentence with more words"
result_s1, result_s2 = remove_common_words(s1, s2)
print("After removing common words:")
print("Sentence 1:", result_s1)
print("Sentence 2:", result_s2)

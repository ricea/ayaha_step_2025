import os
from collections import Counter

path_to_dictionary = 'words.txt'

def make_letter_count_dictionary(path_to_dictionary):
    with open(path_to_dictionary) as f:
        dictionary = [word.rstrip() for word in f.readlines()]
    letter_count_dictionary = []
    for word in dictionary:
        letter_count_dictionary.append((Counter(word),word))
    return letter_count_dictionary

def letter_count(word):
    letter_count_list = Counter(word)
    return letter_count_list

def return_anagram(random_word, letter_count_dictionary):
    random_word_letter_list = letter_count(random_word)
    anagram = []
    
    for i in range(len(letter_count_dictionary)):
        list = letter_count_dictionary[i][0]
        if not(list- random_word_letter_list):
            anagram.append(letter_count_dictionary[i][1])
    
    if len(anagram) == 0:
        return None
    return anagram

def calculate_score(word):
    SCORES = [1, 3, 2, 2, 1, 3, 3, 1, 1, 4, 4, 2, 2, 1, 1, 3, 4, 1, 1, 1, 2, 3, 3, 4, 3, 4]
    score = 0
    for character in list(word):
        score += SCORES[ord(character) - ord('a')]
    return score
          
def highest_score_anagram(anagram):
    scores = {}
    for i in range(len(anagram)):
        scores[anagram[i]] = calculate_score(anagram[i])
            
    best_anagram = [kv[0] for kv in scores.items() if kv[1] == max(scores.values())]
    return best_anagram

def find_best_anagrams(words):
    best_anagram= []
    for i in range(len(words)):
        word = words[i]
        anagram = return_anagram(word,letter_count_dictionary)
        highest_score_anagrams = highest_score_anagram(anagram)
        best_anagram.append(highest_score_anagrams[0])
    return best_anagram
         
if __name__ == "__main__":
    letter_count_dictionary = make_letter_count_dictionary(path_to_dictionary)
    with open('small.txt') as f:
        small_words = [word.rstrip() for word in f.readlines()]
    with open('medium.txt') as f:
        medium_words = [word.rstrip() for word in f.readlines()]
    with open('large.txt') as f:
        large_words = [word.rstrip() for word in f.readlines()]
    
    # small
    best_small_anagram = find_best_anagrams(small_words)
    print(best_small_anagram)
    
    # medium
    best_medium_anagram = find_best_anagrams(medium_words)
    print(best_medium_anagram)
    
    # large
    best_large_anagram = find_best_anagrams(large_words)
    print(best_large_anagram)
    
    with open('small_answer.txt', 'w') as f:
        f.write("\n".join(best_small_anagram))
    with open('medium_answer.txt', 'w') as f:
        f.write("\n".join(best_medium_anagram))
    with open('large_answer.txt', 'w') as f:
        f.write("\n".join(best_large_anagram))
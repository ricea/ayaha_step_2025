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

def return_anagram(random_word, path_to_dictionary):
    random_word_letter_list = letter_count(random_word)
    anagram = []
    
    letter_count_dictionary = make_letter_count_dictionary(path_to_dictionary)
    
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
         
if __name__ == "__main__":
    with open('small.txt') as f:
        small_word = f.read().replace("\n", "")
    with open('medium.txt') as f:
        medium_word = f.read().replace("\n", "")
    with open('large.txt') as f:
        large_word = f.read().replace("\n", "")
    
    # small
    small_anagram = return_anagram(small_word, path_to_dictionary)
    best_small_anagram = highest_score_anagram(small_anagram)
    print(best_small_anagram)
    
    # medium
    medium_anagram = return_anagram(small_word, path_to_dictionary)
    best_mdeium_anagram = highest_score_anagram(medium_anagram)
    
    # large
    large_anagram = return_anagram(large_word, path_to_dictionary)
    best_large_anagram = highest_score_anagram(large_anagram)
    
    with open('small_answer.txt', 'w') as f:
        f.write(best_small_anagram[0])
    with open('medium_answer.txt', 'w') as f:
        f.write(best_mdeium_anagram[0])
    with open('large_answer.txt', 'w') as f:
        f.write(best_large_anagram[0])
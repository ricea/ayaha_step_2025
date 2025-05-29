import os

path_to_new_dictionary = 'new_dictionary.txt'

def make_new_dictionary(path_to_dictionary):
    with open(path_to_dictionary) as f:
        dictionary = [word.rstrip() for word in f.readlines()]
    new_dictionary = []
    for word in dictionary:
        sorted_word = word_sort(word)
        new_dictionary.append(sorted_word, word)
    new_dictionary = sorted(new_dictionary, key = lambda x:(x[0]))
    with open(path_to_new_dictionary, 'w') as f:
        for new_word in new_dictionary:
            f.write(str(new_word[0]) + ',' + str(new_word[1]) + '\n')
    
    
def word_sort(word):
    sorted_word_list = sorted(word)
    return ''.join(sorted_word_list)


def adjust_search(sorted_random_word, new_dictionary, index):
    start = index
    end = index
    while new_dictionary[start][0] == sorted_random_word:
        start -= 1
    while new_dictionary[end][0] == sorted_random_word:
        end += 1
    return [new_dictionary[i][1] for i in range(start+1, end)]


def anagram_binary_search(sorted_random_word, path_to_new_dictionary):
    with open(path_to_new_dictionary) as f:
        new_dictionary = [word.rstrip().split(',') for word in f.readlines()]
    left = 0
    right = len(new_dictionary)-1
    while left <= right:
        mid = (left + right) //2
        if new_dictionary[mid][0] == sorted_random_word:
            return adjust_search(sorted_random_word,new_dictionary,mid)
        elif new_dictionary[mid][0] < sorted_random_word:
            left = mid + 1
        else:
            right = mid - 1 
    return None
    

def return_anagram(random_word, path_to_new_dictionary):
    sorted_random_word = word_sort(random_word)
    
    anagram = anagram_binary_search(sorted_random_word, path_to_new_dictionary)
    return anagram

if __name__ == "__main__":
    if not os.path.exists('new_dictionary.txt'):
        make_new_dictionary('words.txt')
    
    random_word = input()
    print(return_anagram(random_word,path_to_new_dictionary))
   
class Anagram:
    # return list of words.
    def read_words_from_file():
        try:
            with open('wordlist.txt', 'r') as file:
                words_list = file.read().split()
            return words_list
        except FileNotFoundError:
            print("Error: File not found.")
            return []

    # anagram program
    def anagrams(find_anagrams_of_word, word_list):
        anagrams_list = []
        
        # sort the input word alphabetically to test angaisnt dictionary word also sorted alphabetically
        testword = sorted(find_anagrams_of_word.lower())
        # print(testword)
        
        for word in word_list:
            if word != find_anagrams_of_word: # check if word is not the test word its self
                if sorted(word) == testword:
                    anagrams_list.append(word)
        
        return anagrams_list













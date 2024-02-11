from flask import Flask, request
from flask_restful import Resource, Api
from anagram import Anagram
from vocab import convert_to_dict, get_random_definition, get_random_word

app = Flask(__name__)
api = Api(app)

# create the dict of words:definitions
word_dict = convert_to_dict('Majortest.txt')

# find the anagrams of a given word.
class Anagrams(Resource):
    def get(self,myword):
        words = Anagram.read_words_from_file()
        anagrams = Anagram.anagrams(myword, words)

        if not anagrams:
            return {'Anagrams': 'None found in my dictionary'}
        else:
            return {'Anagrams': anagrams}

# select word at random.
class WordToDefinition(Resource):
    def get(self):
        word = get_random_word(word_dict)
        return {'Define':word}
           
# get defintinon of specific word
class WordDefintion(Resource):
    def get(self, word):
        definition = word_dict.get(word.capitalize())
        return {word:definition}

# select definition of a word at random
class DefinitionToWord(Resource):
    def get(self):
        definition = get_random_definition(word_dict)
        return {'What is': definition}

#get word from a specifict definition
#TODO: work out so user's definition doesn't have to match the dictionarys letter for letter.
class DefinitionWord(Resource):
    def get(self, definition):
        pass


api.add_resource(Anagrams, '/getanagram/<string:myword>')
api.add_resource(WordToDefinition,'/randomword')
api.add_resource(WordDefintion, '/define/<string:word>')
api.add_resource(DefinitionToWord, '/whatis')


if __name__ == '__main__':
    app.run(debug=True)

import json
import random

with open('twitter.txt') as data_file:
    data = json.load(data_file)
seed = [data[x]['text'].encode('UTF-8') for x in xrange(len(data))]
seedstring = 'Florida Man '
for x in xrange(len(seed)):
    seedstring += seed[x].split('http', 1)[0] + '.'
with open("database.txt", "w") as text_file:
    text_file.write(seedstring)


class Markovgenerator(object):
    """Generates pseudo random text with markov chains. Math!"""
    def __init__(self, input_file):
        self.cache = {}
        self.input_file = input_file
        self.words = self.file_to_words()
        self.word_size = len(self.words)
        self.database()

    def file_to_words(self):
        data = open(self.input_file, 'r')
        datashtring = data.read().decode('utf-8')
        words = datashtring.split()
        data.close()
        return words

    def triples(self):
        if len(self.words) < 3:
            return

        for i in range(len(self.words) - 2):
            yield (self.words[i], self.words[i+1], self.words[i+2])

    def database(self):
        for (word1, word2, word3) in self.triples():
            key = (word1, word2)
            if key in self.cache:
                self.cache[key].append(word3)
            else:
                self.cache[key] = [word3]

    def generate_markov_text(self, size=25, *start_seed):
        seed = random.randint(0, self.word_size-3)
        seed_word, next_word = self.words[seed], self.words[seed+1]
        if start_seed:
            seed_word, next_word = start_seed[0], start_seed[1]
        word1, word2 = seed_word, next_word
        generated_text = []
        for i in xrange(size):
            generated_text += word1
            word1, word2 = word2, random.choice(self.cache[(word1, word2)])
            generated_text += word2
        return " ".join(generated_text)

starting_data = Markovgenerator('database.txt')
output_text = starting_data.generate_markov_text(25).encode('utf-8')
print output_text
with open("OutputText.txt", "w") as text_file:
    text_file.write(output_text)

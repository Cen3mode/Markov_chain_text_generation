from difflib import SequenceMatcher
from random import choice

text = []

files = [
    "./materials/The Categories by Aristotle.txt",
    "./materials/We're Off to Mars! by Joe Gibson.txt",
]

for text_file in files :
    fl = open(text_file)
    text += fl.read().split()
    fl.close()



class Text_generator:

    def __init__(self, text_table: list, key_size: int = 2):
        self.markov_chain = {}

        self.key_size = key_size

        for word in range(len(text)-self.key_size) :
            key = " ".join(text[word:word + self.key_size])

            if key in self.markov_chain :
                self.markov_chain[key].append(text[word + self.key_size])
            else :
                self.markov_chain[key] = [text[word + self.key_size]]


    def generate_sentence(self) -> str :
        period = False
        start = choice(list(self.markov_chain))
        while start[0].islower() and start[0].isalpha() :
            start = choice(list(self.markov_chain))
        sentence = start

        while not period :
            key = " ".join(sentence.split()[-self.key_size:])
            result = self.markov_chain[key]
            result = choice(list(result))
            sentence += " " + result
            if sentence[-1] == "." :
                break

        return sentence

    def generate_paragraph(self, sentence_count: int = 10) -> str :
        paragraph = ""
        for _ in range(sentence_count) :
            paragraph += self.generate_sentence() + " "
        paragraph += "\n\r"
        return paragraph

gen = Text_generator(text)
print(gen.generate_paragraph())
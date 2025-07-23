import string
from graph import Graph, Vertex
import random
import re
import os

def get_words_from_text(text_path):
    with open(text_path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()

        # remove [text in here]
        text = re.sub(r"\[(.+)\]", " ", text)

        text = " ".join(text.split()) # this turns any kinda split in text into a single white space
        text = text.lower()
        # now we could be complex and deal with punctuation... but there are cases where
        # you might add a period such as (Mr. Brightside), but that's not really
        # punctuation... so we just remove all the punctuation
        text = text.translate(str.maketrans("", "", string.punctuation))

    words = text.split()
    return words

def make_graph(words):
    g = Graph()
    previous_word = None

    # for each word
    for word in words:
        # check that word is in the graph, and if not then add it
        word_vertex = g.get_vertex(word)

        # if there was a previous word, then add an edge if it does not already exist
        # in the graph, otherwise increment weight by 1
        if previous_word:
            previous_word.increment_edge(word_vertex)

        # set our word to the previous word
        previous_word = word_vertex

    # now remember that we want to generate the probability mappings before composing
    # this is a great place to do it before we return the graph object.
    g.generate_probability_mappings()

    return g

def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words)) # pick a random word to start with
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition

def main(artist):
    # step 1: get words from text
    # words = get_words_from_text("texts/hp_sorcerer_stone.txt")
    
    # for song lyrics
    words = []
    for song_file in os.listdir(f"songs/{artist}"):
        if song_file == ".DS_Store":
            continue
        song_words = get_words_from_text(f"songs/{artist}/{song_file}")
        words.extend(song_words)
 
    # step 2: make a graph using those words
    g = make_graph(words)

    # step 3: get the next word for x number of words (defined by user)
    # step 4: show the user the result
    composition = compose(g, words, 100)
    return " ".join(composition) # return a string

if __name__ == "__main__":
    print(main("taylor_swift"))
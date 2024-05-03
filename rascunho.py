import random

def main():
    sentence = make_sentence()
    print(sentence)

def make_sentence():
    determiner = get_determiner()
    noun = get_noun()
    verb = get_verb()
    return f"{determiner} {noun} {verb}"

def get_determiner():
    determiners = ["the", "a", "an"]
    return random.choice(determiners)

def get_noun():
    nouns = ["cat", "dog", "bird"]
    return random.choice(nouns)

def get_verb():
    verbs = ["runs", "jumps", "flies"]
    return random.choice(verbs).capitalize()

main()

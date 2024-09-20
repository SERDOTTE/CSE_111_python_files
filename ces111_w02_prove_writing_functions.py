import random

quantity = [1,2]
quantity = random.choice(quantity) # choose randomly between these two numbers and get the result to the variable

def main():
    for i in range(6): #loop to print six sentenses
        quantity = random.choice([1, 2]) # choose randomly between these two numbers and get the result to the variable for each sentense
        tense = random.choice(["past", "present", "future"]) #main function of the program. Inside it, we use random.choice(["past", "present", "future"]) to randomly choose between "past", "present" and "future" and assign the result to the tense variable
        sentence = make_sentence(quantity, tense)
        print(f"\033[93m{i+1}. {sentence}\033[0m") # Print the sentence with the count from 1 to 6
    
def make_sentence(quantity, tense): #takes two arguments, quantity and tense, and uses these arguments to call functions to get a random determiner, noun, and verb.
    determiner = get_determiner(quantity)
    adjective = get_adjective(quantity)
    noum = get_noum(quantity)
    verb = get_verb(quantity, tense)
    preposition = get_preposition(quantity)
    prepositional_phrase = get_prepositional_phrase(quantity)
    return f"{determiner} {adjective} {noum} {verb} {preposition} {prepositional_phrase}."

def get_determiner(quantity): #choose the determiner randomly according to the quantity variable
    if quantity == 1:
        determiners = ["a", "one", "the"]
    else:
        determiners = ["some", "many", "the"]
    determiner = random.choice(determiners).capitalize()
    return determiner

def get_noum(quantity): #choose the noum randomly according to the quantity variable
    if quantity == 1:
        noums = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        noums = ["birds", "boys", "cars", "children", "dogs", "girls", "men", "rabbits", "women"]
    noum = random.choice(noums)
    return noum

def get_verb(quantity, tense): #choose verb randomly according to the quantity variable
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    verb = random.choice(verbs)
    return verb

def get_preposition(quantity):
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"] 
    preposition = random.choice(prepositions)
    return preposition

def get_prepositional_phrase(quantity):
    determiner = get_determiner(quantity).lower()
    adjective = get_adjective(quantity)
    noum = get_noum(quantity)
    return f"{determiner} {adjective} {noum}"

def get_adjective(quantity):
    adjetcives = ["beautiful", "smart", "happy", "brave", "funny", "tall", "kind"]
    adjective = random.choice(adjetcives)
    return adjective
         
main()
        

        
        
        
        
        
        



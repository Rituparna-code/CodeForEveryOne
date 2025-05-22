import nltk
from nltk import CFG
import matplotlib.pyplot as plt
from nltk import Tree

# Define the CFG for the sentence
grammar = CFG.fromstring("""
    S -> MainClause SubClause | NP VP | NP VP S1 | S Conj S | NP | VP
    S1 -> WH-phrase VP
    WH-phrase -> WH Prep
    WH -> "how"                  
    MainClause -> NP VP 
    SubClause -> Conj NP VP | Rel VP
    NP -> N |N N |AdjP N | N ProperNoun|Quantifier N |Adj NP| ProperNoun | ProperNoun N | Gerund |NP Conj NP | D NP |NP PP| Pronoun |Pronoun NP | Quantifier Adj Adj N | D Adj N
    D -> "this" | "each" | "A" | "a" | "an" | "the"|"The" |"An"| "some"
    Pronoun -> "I" | "There" | "it" | "its" |"your" | "us"  | "you"
    ProperNoun -> "Jagarnath" |"Radhe" | "Ram" | "Sita" | "Puja" | "Sipra" | "It"
    VP -> VP Adv | VP PP | V NP PP Adv | V | Adv VP | V Adv Adj | V NP | V NP Adv| V PP | Aux NP VP | Aux VP | Aux V InfVP |V Adj InfVP | V Pronoun VP
    Aux -> "are" | "is" | "am" |"will" | "be"| "has"
    Quantifier -> "two" | "one"
    AdjP -> Adj Conj Adj
    Rel -> "who"
    Num -> "2022" 
    Adj ->"current" | "past" | "sorry" | "tiring" | "following" | "valuable" | "distinct" | "visual" | "great"
    V -> "teaches" | "solve" | "prepare" | "having" | "handling" | "narrated" | "like" |"touch" |"am" | "hear" | "graduated" | "plucking" | "have" | "let" | "is" | "taking" | "going" | "playing" | "singing" | "said" | "be" | "changes"| "acknowledges" | "likes" |"like" | "created" | "is" | "playing" |"singing"
    InfVP -> Inf V PP
    PP -> PP PP | Prep NP | Prep Num | Prep Gerund Conj Gerund | Prep Gerund | PP NP 
    Adv ->"also" |"today" | "very" | "separately"
    Prep ->  "about" | "to" | "with" | "by" | "of" | "for" |"at" | "with" | "to"    
    Inf -> "to"
    N -> "book" | "problems" | "math" | "timetable" | "branches" | "branch" | "faculty member" | "subjects" | "stories" | "college" | "achievements" |"Alumnus"|"dog" | "flowers" |"flower" | "fun" | "sir" | "mathematics" | "class" | "football" | "temple" | "reference"|"object" | "position" | "respect" | "frame" | "motion" | "reference" |  "manuscript" | "book" | "academics" | "contribution"| "council" | "song" | "football" | "flower" | "boy"|"girl" | "systems" | "rods" | "cones" | "workout"
    Gerund -> "swimming" |"reviewing" | "refining" | "tiring"
    Conj -> "and" | "when" | ";"                  
  
""")

# Create a parser
parser = nltk.ChartParser(grammar)

# Input sentence
# sentence = "A boy with a flower likes the girl".split()
# sentence = "There are two distinct visual systems created by rods and cones".split()
# sentence = "swimming is a great workout".split()
# sentence = "Ram is playing football".split()
# sentence = "Sita is singing a song".split()
sentence = "The council also acknowledges the valuable contribution of the following academics for reviewing and refining the manuscript of the book".split()
# sentence = "Ram is a boy".split()
# sentence = "Sita is singing".split()
# sentence = "An object is said to be at motion when it changes its position with respect to frame of reference".split()
# sentence = "Ram playing".split()
# sentence = "Sita singing".split()
# sentence = "Puja and Sipra are playing football".split()
# sentence = "Puja and Sipra are going to temple".split()
# sentence = "Radhe sir will be taking your mathematics class today".split()
# sentence = "It is very tiring ; let us have some fun".split()
# sentence = "I am sorry to hear about your dog".split()
# sentence = "I touch the flowers".split()
# sentence = "I like flower".split()
# sentence = "I am plucking the flowers".split()
# sentence = "Alumnus Jagarnath has narrated the current and past stories of the college".split()
# sentence = "this book teaches you how to solve math problems".split()
# sentence = "I am plucking the flowers".split()
print(sentence)# Parse the sentence and plot the tree
print("Parsing the sentence...")

for tree in parser.parse(sentence):
    # Display the tree using matplotlib
    tree.pretty_print()
    
    # Plot the tree using matplotlib
    fig = plt.figure(figsize=(10, 10))
    tree.draw()  # This will pop up a window with the tree plot
    plt.show()

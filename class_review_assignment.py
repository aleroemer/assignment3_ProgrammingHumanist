import spacy
from collections import Counter 

nlp = spacy.load("en_core_web_sm")

def count_words(filename):
    with open(filename, encoding = "utf-8") as input_file:
        text = input_file.read()
    doc = nlp(text)
    filtered_words = []
    for token in doc: 
        if token.ent_type_ in ("PERSON", "LOC", "GPE"):
            continue
        if token.pos_ in ("VERB", "ADV"):
            continue
        if token.is_stop:
            continue
        filtered_words.append(token.text)
    word_count = Counter(filtered_words)
    return word_count

dracula_count = count_words("dracula_unique.txt")
great_count = count_words("great_exp_unique.txt")

print(dracula_count)


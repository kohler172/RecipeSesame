import spacy
from collections import Counter

nlp = spacy.load("en_core_web_md")
food = nlp("food")
NOUN_SIM = 0.3
ADJ_SIM = 0.3
keywords = []

with open('recipe1') as f:
    lines = f.readlines()
temp = ' '.join(lines)
recipe1 = nlp(temp)

with open('recipe2') as f:
    lines = f.readlines()
temp = ' '.join(lines)
recipe2 = nlp(temp)

with open('recipe3') as f:
    lines = f.readlines()
temp = ' '.join(lines)
recipe3 = nlp(temp)

while(1):
    lastLine = input("type:")
    doc = nlp(lastLine)
    for chunk in doc.noun_chunks:
        if chunk.similarity(food) > NOUN_SIM:
            keywords.append(chunk.text)

    adjectives = [token.lemma_ for token in doc if token.pos_ == "ADJ"]
    for adj in adjectives:
        chunk = nlp(adj)
        if chunk.similarity(food) > ADJ_SIM:
            keywords.append(chunk)
    print(Counter(keywords))

    temp = ' '.join(keywords)
    print(temp)
    keyNLP = nlp(temp)

    print(keyNLP.similarity(recipe1))
    print(keyNLP.similarity(recipe2))
    print(keyNLP.similarity(recipe3))


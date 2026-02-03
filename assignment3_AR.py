"""
Assignment 3: Text Analysis with SpaCy
Finding distinctive vocabulary between Dracula and Great Expectations
"""

# Import libraries
import spacy
from collections import Counter

# Load Spacy
nlp = spacy.load("en_core_web_sm")
print("Libraries loaded successfully!")

# 1.a Read the Dracula text file                                                                              
with open('dracula.txt', 'r', encoding='utf-8') as file:                                                  
      dracula_text = file.read() 

# Process Dracula text with SpaCy                                                                                
print("\nProcessing Dracula...")                                                                                 
dracula_doc = nlp(dracula_text) 


# 1.b Read Great Expectations text file
with open('great_expectations.txt', "r", encoding='utf-8') as file:
    great_exp_text = file.read()
                                                                                                            
# Process Great Expectations text with SpaCy                                                                                
print("\nProcessing Great Exp...")                                                                                 
great_exp_doc = nlp(great_exp_text) 

# 2. Filter out character, place, verbs and adverbs
## 2.a For Dracula: 
dracula_filtered = []                                                                                            
for token in dracula_doc:                                                                                        
    # Skip if it's a person or place name                                                                        
    if token.ent_type_ in ['PERSON', 'GPE', 'LOC']:                                                              
        continue                                                                                                 
    # Skip if it's a verb or adverb                                                                              
    if token.pos_ in ['VERB', 'ADV']:                                                                            
        continue                                                                                                 
    # Skip punctuation and whitespace                                                                            
    if token.is_punct or token.is_space:                                                                         
        continue                                                                                                 
    # Keep the word (lowercase)                                                                                  
    dracula_filtered.append(token.text.lower())    

print(f"Dracula: {len(dracula_filtered)} words after filtering") 

## 2.b for Great Expectations
great_exp_filtered = []
for token in great_exp_doc:
    if token.ent_type_ in ['PERSON', 'GPE', 'LOC']:
        continue
    if token.pos_ in ['VERB', 'ADV']:
        continue
    if token.is_punct or token.is_space:
        continue
    great_exp_filtered.append(token.text.lower())

print(f"Great Expectations: {len(great_exp_filtered)} words after filtering")

# 3. Count how many times each word appears in Dracula                                                              
dracula_counts = Counter(dracula_filtered)                                                                       
                                                                                                                   
# See the top 10 most common words                                                                               
print("\nTop 10 most common words in Dracula:")                                                                  
print(dracula_counts.most_common(10))                                                                            
                                                                                                                 
# See how many unique words there are                                                                            
print(f"\nTotal unique words in Dracula: {len(dracula_counts)}")  
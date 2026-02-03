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

# Read the Dracula text file                                                                              
with open('dracula.txt', 'r', encoding='utf-8') as file:                                                  
      dracula_text = file.read()                                                                            
                                                                                                            
  # Print the first 500 characters to see what we have                                                      
print(dracula_text[:500]) 

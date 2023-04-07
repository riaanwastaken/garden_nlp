# L3T11 - Compulsary Task 1

# Import the spaCy library
import spacy 

# Load the English language model
nlp = spacy.load('en_core_web_sm')

# Define a list of garden path sentences
gardenpathSentences = [
                        "The horse raced past the barn fell.",
                        "The cotton clothing is usually made of grows in Mississippi.",
                        "The old man the boat sailed away quickly.",
                        "The chicken is ready to eat that was cooking all afternoon.",
                        "The group of friends went to the movie that had some funny scenes.",
                      ]

# Iterate through each sentence in the list
for sentence in gardenpathSentences:
    
    # Tokenize the sentence using the spaCy model
    doc = nlp(sentence)
    
    # Extract the non-punctuation and non-space tokens and print them
    print("\n" + str([token.orth_ for token in doc if not token.is_punct | token.is_space]))
    
    # Iterate through each entity in the sentence and print its label and explanation
    for entity in doc.ents:
        print(f"The entity identified by SpaCy '{entity.text}' as label '{entity.label_}' explained as: {spacy.explain(entity.label_)}\n")


#Comment on Two Entities:

#The code prints out entities in random garden path sentences and their explanations. 
#Two of the entities that were looked up and their explanations are commented on below:

#Entity 1: "Mississippi"

#Explanation: A geopolitical entity, i.e. countries, cities, states.

#Comment: The entity makes sense in the context of the sentence "The cotton 
#clothing is usually made of grows in Mississippi". Mississippi is a state 
#in the United States where cotton is grown and is commonly associated with cotton production.

#Entity 2: "friends"

#Explanation: Group of people.

#Comment: The entity makes sense in the context of the sentence "The group of 
#friends went to the movie that had some funny scenes". The word "friends" 
#indicates a group of people who went to the movie together, which is correctly 
#identified as an entity by SpaCy.

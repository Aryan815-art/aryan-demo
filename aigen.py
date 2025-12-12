import random

text = """
Generative AI is a type of artificial intelligence.
It can create new text, images, and more.
AI learns from data and generates new content.
This is a simple example of how generative text works.
"""

# Split text into words
words = text.split()
word_dict = {}

# Build word connections (Markov chain)
for i in range(len(words) - 1):
    if words[i] in word_dict:
        word_dict[words[i]].append(words[i+1])
    else:
        word_dict[words[i]] = [words[i+1]]

# Generate new text
word = random.choice(words)
sentence = word

for i in range(20):      # generate 20 extra words
    next_words = word_dict.get(word)
    if not next_words:
        break
    next_word = random.choice(next_words)
    sentence += " " + next_word
    word = next_word

print("Generated Text:")
print(sentence)

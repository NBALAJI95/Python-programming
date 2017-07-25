from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tag import pos_tag
import nltk
import heapq

stop = set(stopwords.words('english'))

# Read the file
f = open('TextFile.txt')
sentence = f.read()

# Remove all the words like a the ! ? ... Which does not have meaning using stopwords in NLTK
op = [i for i in word_tokenize(sentence.lower()) if i not in stop and len(i) > 1]
print '\nAfter removal of stopwords \n',op

# Using Lemmatization, apply lemmatization on the remaining words
lmtzr = WordNetLemmatizer()
lemmatized_output = list()
for i in op:
    lemmatized_output.append(lmtzr.lemmatize(i))
print '\nLemmatized output', lemmatized_output

# Using POS, remove all the verbs
pos_output = list()
for tup in pos_tag(lemmatized_output):
    if tup[1][:2] == 'VB':
        continue
    else:
        pos_output.append(tup[0])
print '\nPOS output after verbs removal \n', pos_output

# Calculate the word frequency of the remaining words
word_frequency = nltk.FreqDist(pos_output)
top_five = dict()
for word, frequency in word_frequency.most_common(5):
    top_five[word] = frequency

# Choose top five words that has been repeated most
top_five = top_five.keys()
print '\nTop 5 words that has been repeated most\n', top_five

# Find all the sentences with those most repeated words
op_sentences = list()
for line in sentence.split('\n'):
    for words in top_five:
        if words in line.lower():
            op_sentences.append(line)
            break

# Extract those sentences and concatenate
print '\nFinal output\n', '\n'.join(op_sentences)
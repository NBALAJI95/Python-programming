import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize, sent_tokenize, wordpunct_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.tag import pos_tag
from nltk import ne_chunk, pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
import numpy

def main():
    input_text = 'We will discuss briefly about the basic syntax,\
 structure and design philosophies. \
 There is a defined hierarchical syntax for Python code which you should remember \
 when writing code! Python is a really powerful programming language!'

    #synsets = wn.synsets('phone')
    #print [str(syns.definition()) for syns in synsets]

    synsets = wn.synsets('philosophies')
    for syns in synsets:
        print 'philosophies', '==>', syns.definition()

    synsets = wn.synsets('Python')
    for syns in synsets:
        print 'Python', '==>', syns.definition()

    op = word_tokenize(input_text)
    print '\nTokenize output', op

    print '\nStemming output'
    for e in op:
        if len(e) > 1:
            porter_stemmer = PorterStemmer()
            print porter_stemmer.stem(e)

    print '\nPOS', pos_tag(op)

    print('\nLemmatize output')
    lm = WordNetLemmatizer()
    for e in op:
        if len(e) > 1:
            print lm.lemmatize(e)

    print '\nTrigram output'

    trigrams = ngrams(op, 3)
    for grams in trigrams:
        print grams

    print '\nNamed Entity Recognization'
    print ne_chunk(pos_tag(wordpunct_tokenize(input_text)))

if __name__ == '__main__':
    main()
class TextCleaner:
    '''Cleans text for Analysis.'''
    
    def __init__(self):
        pass
    
    def remove_characters_before_tokenization(sentence,
         keep_apostrophes=False):
        
         '''
         remove_characters_before_tokenization('Test sentence 1 2 3 4 @')
         >>> Test sentence 1 2 3 4
         '''
        
         sentence = sentence.strip()
         if keep_apostrophes:
             PATTERN = r'[?|$|&|*|%|@|(|)|~]' # add other characters here to remove them
             filtered_sentence = re.sub(PATTERN, r'', sentence)
         else:
             PATTERN = r'[^a-zA-Z0-9 ]' # only extract alpha-numeric characters
             filtered_sentence = re.sub(PATTERN, r'', sentence)
         return filtered_sentence 
    
    def expand_contractions(sentence, contraction_mapping):
         '''
          expand_contractions("This is a test sentence. But this isn't one. hasn't she hearten?", CONTRACTION_MAP)
          >>> This is a test sentence. But this is not one. has not she hearten?
         '''
         contractions_pattern = re.compile('({})'.format('|'.join(contraction_mapping.keys())),
         flags=re.IGNORECASE|re.DOTALL)
            
         def expand_match(contraction):
             match = contraction.group(0)
             first_char = match[0]
             expanded_contraction = contraction_mapping.get(match)\
                 if contraction_mapping.get(match)\
                 else contraction_mapping.get(match.lower())
             expanded_contraction = first_char+expanded_contraction[1:]
             return expanded_contraction
         expanded_sentence = contractions_pattern.sub(expand_match, sentence)
         return expanded_sentence 
        
    def remove_stopwords(tokens):
         '''
        remove_stopwords(nltk.word_tokenize("This is a test sentence. But this isn't one. hasn't she hearten?".lower()))
        >>> ['test', 'sentence', '.', "n't", 'one', '.', "n't", 'hearten', '?']
         '''
         stopword_list = nltk.corpus.stopwords.words('english')
         filtered_tokens = [token for token in tokens if token not in stopword_list]
         return filtered_tokens 
        
    def stat_text_analysis(test_data):
        '''
        Returns list of statistical text test results.
        '''
        fre = textstat.flesch_reading_ease(test_data)
        si = textstat.smog_index(test_data)
        fkg = textstat.flesch_kincaid_grade(test_data)
        cli = textstat.coleman_liau_index(test_data)
        ari = textstat.automated_readability_index(test_data)
        dcri = textstat.dale_chall_readability_score(test_data)
        dw = textstat.difficult_words(test_data)
        lwf = textstat.linsear_write_formula(test_data)
        gf = textstat.gunning_fog(test_data)
        ts = textstat.text_standard(test_data)
        
        return ([
            ['fre', fre],
            ['si', si],
            ['fkg', fkg],
            ['cli', cli],
            ['ari', ari],
            ['dcri', dcri],
            ['dw', dw],
            ['lwf', lwf],
            ['gf', gf],
            ['ts', ts],            
                ])
    
    def word_freq_pair(wordstring):
        '''
        print((word_freq_pair('this is a test sentence is is is.')))
        [('this', 1), ('is', 3), ('a', 1), ('test', 1), ('sentence', 1), ('is', 3), ('is', 3), ('is.', 1)]
        '''
        wordlist = wordstring.split()

        wordfreq = []

        for w in wordlist:
            wordfreq.append(wordlist.count(w))

        return list(zip(wordlist, wordfreq))
    
    
    def removeStopwords(wordlist):
        '''
        removeStopwords("this is a test sentence.".split(" "))
        >>> ['test', 'sentence.']
        '''
        return [w for w in wordlist if w not in nltk.corpus.stopwords.words('english')]
    
    
    

    def nGramsToKWICDict(ngrams):
        '''
        ngrams = obo.getNGrams('this test sentence has eight words in it'.split(), 5)
        print(ngrams)
        >>> [['this', 'test', 'sentence', 'has', 'eight'],
             ['test', 'sentence', 'has', 'eight', 'words'],
             ['sentence', 'has', 'eight', 'words', 'in'],
             ['has', 'eight', 'words', 'in', 'it']]
        '''
        keyindex = len(ngrams[0]) // 2

        return keyindex
    
    
    def nGramsToKWICDict(ngrams):
        '''
        print(nGramsToKWICDict(
                             [['this', 'test', 'sentence', 'has', 'eight'],
                             ['test', 'sentence', 'has', 'eight', 'words'],
                             ['sentence', 'has', 'eight', 'words', 'in'],
                             ['has', 'eight', 'words', 'in', 'it']]
                             ))
                             
        >>> {'words': [['has', 'eight', 'words', 'in', 'it']], 
            'sentence': [['this', 'test', 'sentence', 'has', 'eight']], 
            'has': [['test', 'sentence', 'has', 'eight', 'words']], 
            'eight': [['sentence', 'has', 'eight', 'words', 'in']]}
        
        '''
        keyindex = len(ngrams[0]) // 2

        kwicdict = {}

        for k in ngrams:
            if k[keyindex] not in kwicdict:
                kwicdict[k[keyindex]] = [k]
            else:
                kwicdict[k[keyindex]].append(k)
        return kwicdict
    
    def get_n_grams(allMyWords, n):
        return obo.getNGrams(allMyWords, n)
    
    def getNGrams(wordlist, n):
        '''
        tNGrams(test2.split(), 5)
        # -> [['this', 'test', 'sentence', 'has', 'eight'],
        # ['test', 'sentence', 'has', 'eight', 'words'],
        # ['sentence', 'has', 'eight', 'words', 'in'],
        # ['has', 'eight', 'words', 'in', 'it']]
        '''
        ngrams = []
        for i in range(len(wordlist)-(n-1)):
            ngrams.append(wordlist[i:i+n])
        return ngrams
    
    
    
    def clean_tweet(tweet):
        '''
        Utility function to clean the text in a tweet by removing 
        links and special characters using regex.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def analize_sentiment(tweet):
        '''
        Utility function to classify the polarity of a tweet
        using textblob.
        '''
        analysis = TextBlob(clean_tweet(tweet))
        if analysis.sentiment.polarity > 0:
            return 1
        elif analysis.sentiment.polarity == 0:
            return 0
        else:
            return -1
        
    def cln_twt(twt):
        return p.clean(twt)
    
    def tkn_twt(twt):
        return p.tokenize(twt)
    
    def prs_twt(twt):
        return p.parse(twt)
    
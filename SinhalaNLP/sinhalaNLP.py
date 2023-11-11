import re
class Stopwords:
    # default constructor
    def __init__(self) -> None:
        stopwords_txt = open('./stopwords.txt', 'r', encoding='utf8')
        stopwordslist = stopwords_txt.readlines()
        stopwords_txt.close() 
        self.sinhala_stopwords = []
        for word in range(0, len(stopwordslist)):
            temp = re.sub('[\n]', ' ', stopwordslist[word])
            temp = re.sub('r[a-zA-A0-9]', ' ', temp)
            temp = temp.strip()
            self.sinhala_stopwords.append(temp)
        self.sinhala_stopwords[17] = 'හෝ'
        self.sinhala_stopwords[29] = 'ශ්රී'
        
        
class SinhalaLemmatizer:
    def __init__(self) -> None:
        lem = open('./lemmatizer.txt', 'r', encoding="utf8")
        lemmatizerlist = lem.readlines()
        lem.close()
        self.word0 = []
        self.word1 = []

        for i in range(0, len(lemmatizerlist)):
            x = lemmatizerlist[i].split()[0]
            y = lemmatizerlist[i].split()[1]
            self.word0.append(x)
            self.word1.append(y)
            
    def lemmertizer(self, word: str) -> str:
        if word in self.word0:
            index = self.word0.index(word)
            return self.word1[index]
        

        
    

        
    
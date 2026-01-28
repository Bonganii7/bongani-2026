from collections import Counter
from typing import List

class WordFreq:

    def __init__(self,n: int = 10):
        self.n = n
        self.counts = Counter()
    """
    
    """


    def process(self, word: str) -> None:

        cleaned = word.strip().lower()
        if cleaned:
            self.counts[cleaned] += 1


    def top_n_words(self) -> List[str]:
        """
        we will return only the top n words as list therefore, strings!
        """
        result = []
        pairs = self.counts.most_common(self.n) # get word and count pairs here kinda like [('luminosity', 5), ('protons', 2)]
        for (word,count) in pairs:
            result.append(word)
        return result



    def top_with_counts(self) -> List[tuple]:

        return self.counts.most_common(self.n)









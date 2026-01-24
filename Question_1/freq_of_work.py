from collections import Counter
from typing import List

class WordFreq:
    """
    Maintain the top N most frequent words in a streaming fashion.
    Args:
        n (int): number of top frequent words to track (default = 10)
    """
    def __init__(self,n: int = 10):
        self.n = n
        self.counts = Counter()

    def process(self, word: str) -> None:
        """
        Process a single word and update the internal frequency counts.
        Args:
            word(str): the word to process
        """
        cleaned = word.strip().lower()
        if cleaned:
            self.counts[cleaned] += 1

    def top(self) -> List[str]:
        """
        Return only the top N words
        """
        return [w for w, _ in self.counts.most_common(self.n)]

    def top_with_counts(self) -> List[tuple]:
        """
        Return the top N words along with their counts.
        Useful for debugging and interviews.
        """
        return self.counts.most_common(self.n)








import unittest
from Question_1.freq_of_work import WordFreq

class TestWordFreq(unittest.TestCase):
    def test_basic(self):
        wf = WordFreq(n=2)
        words = ["apple", "banana", "pear", "banana", "apple"]

        for w in words:
            wf.process(w)

        self.assertEqual(wf.top(), ["apple", "banana"])

if __name__ == "__main__":
    unittest.main()

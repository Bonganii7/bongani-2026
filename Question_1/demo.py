import re
from freq_of_work import WordFreq


if __name__ == "__main__":
    text =("We are part of this universe, we are in this universe,"
           " but perhaps more important than both of those facts"
           "is that the universe is in us")
    wf = WordFreq(n=5)

    words = re.findall(r"[a-zA-Z]+", text.lower())

    for word in words:
        wf.process(word)

    print("Top words:", wf.top_n_words())
    print("Top words:", wf.top_with_counts())





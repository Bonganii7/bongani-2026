from freq_of_work import WordFreq


if __name__ == "__main__":
    text ="the quick brown fox jumps over the lazy dog the fox was quick"
    wf = WordFreq(n=3)

    for word in text.split():
        wf.process(word)

    print("Top words:", wf.top_with_counts())


class Cleaner:

    def __init__(self, text, stopwords):
        self.stopwords = stopwords
        self.text = text

    def clean(self):
        return self.text

    def lemmatize(self):
        return self.text

    def clean_and_lemmatize(self):
        self.clean()
        self.lemmatize()
        return self.text

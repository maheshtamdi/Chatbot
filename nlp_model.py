# nlp_model.py
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

class NLPModel:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.model = MultinomialNB()

    def train(self, X_train, y_train):
        X_vec = self.vectorizer.fit_transform(X_train)
        self.model.fit(X_vec, y_train)
        print("✅ NLP model trained successfully")

    def predict(self, text):
        X_vec = self.vectorizer.transform([text])
        return self.model.predict(X_vec)[0]

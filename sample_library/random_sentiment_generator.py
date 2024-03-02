import random

class RandomSentimentGenerator:
    def generate_random_sentiment():
        sentiments = ['happy', 'sad', 'neutral']
        return random.choice(sentiments)
    
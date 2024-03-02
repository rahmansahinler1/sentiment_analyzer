from sample_library.random_sentiment_generator import RandomSentimentGenerator

for _ in range(10):
    sentiment = RandomSentimentGenerator.generate_random_sentiment()
    print(sentiment)

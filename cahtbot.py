import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Předdefinované odpovědi
responses = ["Ano", "Ne", "Možná", "Dobře", "Nerozumím", "Zkusme něco jiného"]

# Přivítání uživatele
def welcome():
    welcome_messages = ["Vítejte! Jsem chatbot. Jak Vám mohu pomoci?",
                        "Ahoj! Jak Vám mohu pomoci dnes?",
                        "Dobrý den! Jak Vám mohu pomoci?"]
    return random.choice(welcome_messages)

# Zpracování dotazu uživatele
def process_query(query):
    # Předdefinované vzory dotazů
    patterns = ['ahoj', 'dobře', 'pomoc']

    # Vytvoření vektorizéru a transformace dotazu
    vectorizer = CountVectorizer().fit_transform(patterns + [query])
    vectors = vectorizer.toarray()
    query_vector = vectors[-1]

    # Výpočet podobnosti dotazu s předdefinovanými vzory
    similarities = cosine_similarity(query_vector.reshape(1, -1), vectors[:-1])
    max_similarity = similarities.max()

    # Výběr odpovědi s nejvyšší podobností
    if max_similarity < 0.2:
        return random.choice(responses)
    else:
        index = similarities.argmax()
        return responses[index]

# Hlavní funkce chatovacího bota
def chatbot():
    print(welcome())

    while True:
        query = input("Zadejte dotaz: ")
        if query.lower() == "konec":
            print("Děkuji za použití chatbotu. Mějte pěkný den!")
            break
        else:
            response = process_query(query)
            print(response)

# Spuštění chatovacího bota
chatbot()

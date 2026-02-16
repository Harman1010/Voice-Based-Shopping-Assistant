from transformers import pipeline
import re

# Lightweight zero-shot model (faster than large BART)
classifier = pipeline(
    "zero-shot-classification",
    model="valhalla/distilbart-mnli-12-3"
)

INTENTS = ["add", "remove", "modify", "search"]

IGNORE_WORDS = {
    "add", "remove", "modify", "buy", "need",
    "want", "to", "my", "list", "under",
    "for", "please", "find"
}

WORD_NUM = {
    "one": 1, "two": 2, "three": 3,
    "four": 4, "five": 5, "six": 6
}


def detect_intent(text, threshold=0.5):
    result = classifier(text, INTENTS)
    label = result["labels"][0]
    score = result["scores"][0]
    if score < threshold:
        return "unknown"
    return label


def extract_quantity(text):
    number = re.search(r"\b\d+\b", text)
    if number:
        return int(number.group())

    for word in WORD_NUM:
        if word in text.lower():
            return WORD_NUM[word]

    return 1


def extract_price_limit(text):
    match = re.search(r"under\s?\$?(\d+)", text.lower())
    if match:
        return int(match.group(1))
    return None


def extract_item(text):
    text = text.lower()

    import string
    text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()

    
    verbs = ["add", "remove", "modify", "find", "buy"]

    words = [w for w in words if w not in verbs]

    
    words = [w for w in words if not w.isdigit() and w not in WORD_NUM]

    
    stop_words = ["to", "from", "under", "in", "on"]

    item_words = []
    for w in words:
        if w in stop_words:
            break
        item_words.append(w)

    return " ".join(item_words).strip()



def parse_command(text):
    return {
        "intent": detect_intent(text),
        "item": extract_item(text),
        "quantity": extract_quantity(text),
        "price_limit": extract_price_limit(text)
    }

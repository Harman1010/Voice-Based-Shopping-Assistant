
import gradio as gr
from transformers import pipeline
from nlp_engine import parse_command
from categorize import categorize
from recommender import (
    frequency_suggestions,
    seasonal_suggestions,
    substitute_suggestions
)

# Whisper for multilingual voice recognition
asr = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-base"
)

shopping_list = {}
history = []


def search_products(item, price_limit):
    mock_products = [
        {"name": "organic apples", "price": 4},
        {"name": "regular apples", "price": 2},
        {"name": "premium toothpaste", "price": 6}
    ]

    results = []
    for product in mock_products:
        if item in product["name"]:
            if price_limit is None or product["price"] <= price_limit:
                results.append(product)
    return results


def process_audio(audio):
    if audio is None:
        return "No audio detected.", "", ""

    try:
        text = asr(audio)["text"]
    except Exception:
        return "Speech recognition failed. Try again.", "", ""

    parsed = parse_command(text)

    intent = parsed["intent"]
    item = parsed["item"]
    quantity = parsed["quantity"]
    price_limit = parsed["price_limit"]

    message = f"Recognized: {text}\nIntent: {intent}\n"

    if intent == "add":
        shopping_list[item] = shopping_list.get(item, 0) + quantity
        history.append(item)
        message += f"Added {quantity} {item}."

    elif intent == "remove":
        shopping_list.pop(item, None)
        message += f"Removed {item}."

    elif intent == "modify":
        shopping_list[item] = quantity
        message += f"Updated {item} to {quantity}."

    elif intent == "search":
        results = search_products(item, price_limit)
        return (
            message,
            str(results),
            format_suggestions(item)
        )

    category = categorize(item)

    return (
        message + f"\nCategory: {category}",
        format_shopping_list(),
        format_suggestions(item)
    )


def format_shopping_list():
    if not shopping_list:
        return "Shopping list is empty."

    return "\n".join(
        [f"{item} - {qty}" for item, qty in shopping_list.items()]
    )


def format_suggestions(item):
    suggestions = {
        "Frequent": frequency_suggestions(history),
        "Seasonal": seasonal_suggestions(),
        "Substitutes": substitute_suggestions(item)
    }

    return "\n".join(
        [f"{key}: {value}" for key, value in suggestions.items()]
    )


with gr.Blocks() as app:
    gr.Markdown("# 🛒 Voice Command Shopping Assistant")
    gr.Markdown("Speak your shopping command below.")

    gr.Markdown("""
    ### Example Commands
    1. Add 2 apples   
    2. Remove milk  
    3. Modify apples to 5
    """)


    audio_input = gr.Audio(type="filepath", label="Speak Command")
    status_output = gr.Textbox(label="System Feedback")
    list_output = gr.Textbox(label="Shopping List")
    suggestions_output = gr.Textbox(label="Suggestions")

    audio_input.change(
        process_audio,
        inputs=audio_input,
        outputs=[status_output, list_output, suggestions_output],
        show_progress=True
    )

app.launch()

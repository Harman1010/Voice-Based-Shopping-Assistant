# Voice-Based-Shopping-Assistant
A Voice based Shopping Assistant that helps in Smart Shopping
This project is a voice-based shopping list manager powered by Hugging Face Transformers and Gradio. It enables users to manage their shopping list using natural language voice commands with intelligent recommendations and real-time feedback.

The application integrates automatic speech recognition (ASR), zero-shot intent classification, and a rule-based recommendation engine to provide a complete AI-powered shopping assistant experience.

**Features**

**Voice Input**

Multilingual speech recognition using Whisper

Natural language understanding via zero-shot classification

Flexible phrasing support (e.g., “Add milk”, “I want to buy apples”)

**Shopping List Management**

Add / Remove / Modify items

Voice-based quantity handling

Automatic item categorization (Dairy, Produce, Snacks, etc.)

**Voice-Based Search**

Search items via voice

Price range filtering (e.g., “Find toothpaste under $5”)

**Smart Suggestions**

Frequency-based recommendations

Seasonal item suggestions

Substitute recommendations (e.g., almond milk for milk)

**Architecture**

**Voice Input**

1.Whisper (Speech-to-Text)

2.Zero-shot Intent Classification

3.Command Parsing

4.Shopping List Engine

5.Recommendation Engine

6.Gradio UI

**Deployment**

The application is deployed on Hugging Face Spaces (Gradio).

Note: On free-tier hosting, the Space may take a few seconds to start if idle.

**Design Decisions**

Used pretrained transformer models to enable rapid development.

Selected lightweight models for performance on CPU.

Implemented modular architecture for maintainability.

Focused on reliability and clean separation of concerns.

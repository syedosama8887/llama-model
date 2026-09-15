# BlenderBot Chat API

A FastAPI endpoint that generates text with Hugging Face's `facebook/blenderbot-400M-distill` model.

## Overview

`GET /chatbot?question=Hello` generates a response and returns `{"result": "..."}`. The model and tokenizer load when the module is imported. Conversation history is held in one process-wide list, so requests from different users share state.

## Tech stack

Python, FastAPI, Uvicorn, Hugging Face Transformers, and a PyTorch backend.

## Structure

- `main.py` — FastAPI application.
- `api/v1/chatbot.py` — model loading, conversation history, and route.
- `requirements.txt` — dependencies for this application.

## Installation and usage

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

On Windows activate with `.venv\Scripts\activate`. The first start downloads model files and requires network access and enough memory. Visit `http://127.0.0.1:8000/docs` for the route.

## Limitations

This is BlenderBot, not a Llama or OpenAI API integration. There is no user isolation, persistence, authentication, or verified production deployment. No application secrets or environment variables are currently read.

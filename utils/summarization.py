"""
Utility functions for text summarization using Hugging Face transformers.
"""
from transformers import pipeline
import config

_loaded_summarizers = {}
def load_summarizer(model_name):
    if model_name not in _loaded_summarizers:
        _loaded_summarizers[model_name] = pipeline("summarization", model=model_name)
    return _loaded_summarizers[model_name]

# def summarize_text(text, model_name="t5-base", max_len=150):
#     summarizer = pipeline("summarization", model=model_name)
#     return summarizer(text, max_length=max_len, min_length=40, do_sample=False)[0]['summary_text']

# preferred modal for cpu
# Preload the summarizer model at module load
summarizer = pipeline(
    "summarization",
    model=config.TEXT_SUMMARIZATION_MODEL
)

def summarize_text(text, max_len=config.MAX_TEXT_LENGTH):
    """
    Summarize text using preloaded model.
    """
    if not text:
        return ""
    return summarizer(
        text,
        max_length=max_len,
        min_length=config.MIN_TEXT_LENGTH,
        do_sample=False
    )[0]['summary_text']

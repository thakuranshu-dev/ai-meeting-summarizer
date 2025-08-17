from transformers import pipeline

# def summarize_text(text, model_name="t5-base", max_len=150):
#     summarizer = pipeline("summarization", model=model_name)
#     return summarizer(text, max_length=max_len, min_length=40, do_sample=False)[0]['summary_text']

# preferred modal for cpu
def summarize_text(text, model_name="t5-small", max_len=100):
    """
    Summarize text using T5-small (lightweight).
    """
    if not text:
        return ""
    else:
        summarizer = pipeline("summarization", model=model_name)
        return summarizer(
            text,
            max_length=max_len,
            min_length=30,
            do_sample=False
        )[0]['summary_text']

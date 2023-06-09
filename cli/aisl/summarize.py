import logging
logger = logging.getLogger("aisl")

from transformers import pipeline

def summarize(text: str):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    return summarizer(text, max_length=130, min_length=30, do_sample=False)

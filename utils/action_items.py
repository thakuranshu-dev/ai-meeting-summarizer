"""
Utility functions for extracting action items from meeting transcripts.
"""
import re

def extract_action_items(transcript):
    """
    Simple rule-based extractor for action items from meeting transcript.
    Looks for sentences starting with verbs or containing deadlines.
    """

    # Split into sentences (very naive split)
    sentences = re.split(r'(?<=[.!?]) +', transcript)

    # Keywords and patterns that often indicate action items
    action_keywords = [
        "will", "should", "need to", "must", "plan to", "follow up", "complete", "finalize", "prepare"
    ]
    deadline_patterns = [
        r"by \w+day", r"by \d{1,2}(st|nd|rd|th)", r"by end of", r"next week"
    ]

    action_items = []

    for sent in sentences:
        sent_lower = sent.lower()
        if any(kw in sent_lower for kw in action_keywords) or \
           any(re.search(pattern, sent_lower) for pattern in deadline_patterns):
            action_items.append(sent.strip())

    return action_items

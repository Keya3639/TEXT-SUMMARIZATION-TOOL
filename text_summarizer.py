from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from collections import Counter
import re

def detect_topic(text):

    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
    if not words:
        return "General"
    word_freq = Counter(words)

    most_common_word, freq = word_freq.most_common(1)[0]
    return most_common_word.capitalize()

def summarize_text(text, sentence_count=4):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, sentence_count)

    topic = detect_topic(text)
    intro = f"This text is about {topic}. "

    return intro + " ".join(str(sentence) for sentence in summary)

#  User input
print("Input the text here:\n")
import sys
input_text = sys.stdin.read()

#  Summarize + detect topic
summary = summarize_text(input_text, sentence_count=4)


print("\n Summarized Text:\n", summary)

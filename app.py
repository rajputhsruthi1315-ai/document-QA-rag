from pathlib import Path
import re

document = Path("sample_docs/return_policy.txt").read_text(encoding="utf-8")
sentences = re.split(r"(?<=[.!?])\s+", document)

question = input("Ask a question: ")
question_words = set(re.findall(r"\b\w+\b", question.lower()))
stop_words = {"a", "an", "the", "i", "do", "does", "is", "can", "how", "my", "to", "of"}
question_words -= stop_words

def score(sentence):
    sentence_words = set(re.findall(r"\b\w+\b", sentence.lower()))
    return len(question_words & sentence_words)

best_sentence = max(sentences, key=score)

if score(best_sentence) > 0:
    print(f"Answer from document: {best_sentence}")
else:
    print("I couldn't find an answer in the document.")

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from fetch import fetch_article
from consts import Keys
import numpy as np

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
model = AutoModelForSequenceClassification.from_pretrained("bucketresearch/politicalBiasBERT")

def analyze_bias(text: str):
    paragraphs = text.split('\n\n')
    results = {}
    results[Keys.bias] = 0
    total_bias = np.zeros(3)

    for paragraph in paragraphs:
        chunks = split_paragraph(paragraph)
        chunk_bias = np.zeros(3)

        for chunk in chunks:
            inputs = tokenizer(chunk, return_tensors="pt", truncation = True, max_length=512)

            labels = torch.tensor([0])
            outputs = model(**inputs, labels=labels)
            loss, logits = outputs[:2]
            softmax_score = logits.softmax(dim=-1)[0].tolist()

            softmax_score = np.array(softmax_score)
            chunk_bias = np.add(chunk_bias, softmax_score)

        paragraph_bias = np.divide(chunk_bias, len(chunks))
        total_bias = np.add (total_bias, paragraph_bias)
        results[paragraph] = paragraph_bias
        print(paragraph_bias)
    
    total_bias = np.divide(total_bias, len(paragraphs))
    results[Keys.bias] = total_bias
    print(total_bias)
    
    return results

def split_paragraph(paragraph, max_length=500):
    words = paragraph.split()  # Split paragraph by words
    chunks = []
    chunk_text = ""

    for word in words:
        # Add word to chunk and check token length
        temp_chunk = f"{chunk_text} {word}".strip()
        token_count = len(tokenizer.encode(temp_chunk, add_special_tokens=False))

        if token_count <= max_length:
            chunk_text = temp_chunk
        else:
            # If adding the word exceeds max tokens, finalize the current chunk
            chunks.append(chunk_text)
            chunk_text = word  # Start new chunk with the current word

    # Add the last chunk if not empty
    if chunk_text:
        chunks.append(chunk_text)

    return chunks

    
print(analyze_bias(fetch_article("Donald Trump")))
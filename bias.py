from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from fetch import fetch_article
from consts import JSON, Bias
import numpy as np
import json

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
model = AutoModelForSequenceClassification.from_pretrained("bucketresearch/politicalBiasBERT")

def analyze_bias(text: str):
    paragraphs = text.split('\n\n')
    results = {}

    # [0] -> left 
    # [1] -> right
    results[JSON.bias_key] = []
    total_bias = np.zeros(2)

    for paragraph in paragraphs:
        chunks = split_paragraph(paragraph)
        chunk_bias = np.zeros(2)

        for chunk in chunks:
            inputs = tokenizer(chunk, return_tensors="pt", truncation = True, max_length=512)

            labels = torch.tensor([0])
            outputs = model(**inputs, labels=labels)
            loss, logits = outputs[:2]
            softmax_score = logits.softmax(dim=-1)[0].tolist()

            # convert to np array and delete centrist
            softmax_score = np.delete(np.array(softmax_score), 1)
            
            # add chunk bias
            chunk_bias = np.add(chunk_bias, softmax_score)

        # ensure divison by 0 doesn't occur
        if len(chunks) > 0:
            paragraph_bias = np.divide(chunk_bias, len(chunks))
            total_bias = np.add(total_bias, paragraph_bias)

            paragraph 
            # assign side to paragraph if passing threshold
            if max(paragraph_bias[0], paragraph_bias[1]) > Bias.side_threshold:
                entry = {}
                entry[JSON.text_key] = paragraph

                if paragraph_bias[0] > paragraph_bias[1]:
                    # left
                    entry[JSON.side_key] = JSON.side_left_value
                    entry[JSON.confidence_key] = paragraph_bias[0]
                else:
                    # right
                    entry[JSON.side_key] = JSON.side_right_value
                    entry[JSON.confidence_key] = paragraph_bias[1]

                results[JSON.bias_key].append(entry)

    # ensure divison by 0 doesn't occur
    if len(paragraphs) > 0:
        total_bias = np.divide(total_bias, len(paragraphs))

    page_entry = {}
    if total_bias[0] > total_bias[1]:
        # left
        page_entry[JSON.side_key] = JSON.side_left_value
        page_entry[JSON.confidence_key] = total_bias[0]
    else:
        # right
        page_entry[JSON.side_key] = JSON.side_right_value
        page_entry[JSON.confidence_key] = total_bias[1]

    results[JSON.page_key] = page_entry
    
    return json.dumps(results, sort_keys = False)

def split_paragraph(paragraph, max_length=500):
    words = paragraph.split()
    chunks = []
    chunk_text = ""
    
    for word in words:
        temp_chunk = f"{chunk_text} {word}".strip()
        token_count = len(tokenizer.encode(temp_chunk, add_special_tokens=False))

        if token_count <= max_length:
            chunk_text = temp_chunk
        else:
            chunks.append(chunk_text)
            chunk_text = word

    if chunk_text:
        chunks.append(chunk_text)
        
    return chunks
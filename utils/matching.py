import torch
from sentence_transformers import SentenceTransformer, util

class SentenceMatcher:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def encode_sentences(self, sentences):
        return self.model.encode(sentences, convert_to_tensor=True)

    def match_sentences(self, sentence1, sentence2):
        embeddings1 = self.encode_sentences([sentence1])
        embeddings2 = self.encode_sentences([sentence2])
        cosine_scores = util.pytorch_cos_sim(embeddings1, embeddings2)
        return cosine_scores.item()

# Example usage:
# matcher = SentenceMatcher()
# score = matcher.match_sentences('This is a test.', 'This is a test too.')
# print(f'Cosine Similarity Score: {score}')
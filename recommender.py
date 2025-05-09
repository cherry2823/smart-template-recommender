import json
import openai
import numpy as np
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def load_templates(file_path="templates.json"):
    """
    Load the design templates from a JSON file.
    Each template includes title, description, and tags.
    """
    with open(file_path, "r") as f:
        return json.load(f)

def embed_text(text):
    """
    Use OpenAI's text-embedding-ada-002 model to generate an embedding vector for the input text.
    """
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return np.array(response["data"][0]["embedding"])

def compute_similarity(query_vec, vecs):
    """
    Compute cosine similarity between the user query vector and all template vectors.
    """
    return np.dot(vecs, query_vec) / (
        np.linalg.norm(vecs, axis=1) * np.linalg.norm(query_vec) + 1e-10
    )

def recommend_templates(user_input, top_k=3):
    """
    Recommend top-k templates based on user input.
    Steps:
      - Embed the user input
      - Embed all templates using title + tags
      - Compute cosine similarity
      - Return the top-k most relevant templates
    """
    templates = load_templates()
    query_vec = embed_text(user_input)

    # Combine title and tags for each template as input to embedding
    template_texts = [t["title"] + " " + " ".join(t["tags"]) for t in templates]
    template_vecs = np.array([embed_text(text) for text in template_texts])

    # Calculate similarity and get top results
    sims = compute_similarity(query_vec, template_vecs)
    ranked_indices = sims.argsort()[::-1][:top_k]
    recommendations = [templates[i] for i in ranked_indices]

    return recommendations

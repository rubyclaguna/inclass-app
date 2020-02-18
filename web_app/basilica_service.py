import os
from dotenv import load_dotenv
import basilica 

load_dotenv()

basilica_api_key = os.getenv("basilica_api_key", default="OOPS")

sentences = [
    "This is a sentence!", 
    "This is a similar sentence!",
    "I don't think this sentence is very similar at all...", 
]

with basilica.Connection('9347f584-35f0-742b-93a1-57ce0f14a19b') as c:
    embeddings = list(c.embed_sentences(sentences))

print(embeddings)
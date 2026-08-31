# embeddings.py
import os
import warnings
from typing import List, Optional

# Optional dependency imports
try:
    from langchain.embeddings import OpenAIEmbeddings
except Exception:
    try:
        from langchain.embeddings.openai import OpenAIEmbeddings
    except Exception:
        OpenAIEmbeddings = None

import requests


class MistralEmbeddings:
    """
    Simple HTTP-based Mistral embeddings wrapper.
    You must set MISTRAL_API_KEY and MISTRAL_EMBEDDING_URL (the embeddings endpoint).
    The exact payload/response format depends on Mistral's API; adjust parsing if needed.
    """

    def __init__(self, api_key: Optional[str] = None, url: Optional[str] = None, model: Optional[str] = None, timeout: int = 30):
        self.api_key = api_key or os.environ.get("MISTRAL_API_KEY")
        self.url = url or os.environ.get("MISTRAL_EMBEDDING_URL")
        self.model = model or os.environ.get("MISTRAL_EMBEDDING_MODEL", "mistral-embedding-1")
        self.timeout = timeout

        if not self.api_key or not self.url:
            raise ValueError("Mistral API key and URL are required (MISTRAL_API_KEY, MISTRAL_EMBEDDING_URL).")

        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def _call_api(self, inputs: List[str]) -> List[List[float]]:
        """
        POSTs to the Mistral embeddings endpoint and returns list of vectors.
        Adjust request/response parsing to match the actual Mistral API.
        """
        payload = {
            "model": self.model,
            # Many embedding APIs expect "input" or "inputs" — adjust as needed.
            "input": inputs,
        }

        resp = requests.post(self.url, json=payload, headers=self.headers, timeout=self.timeout)
        resp.raise_for_status()
        data = resp.json()

        # Common embedding response shapes:
        # - { "data": [ {"embedding": [...]}, ... ] }
        # - { "embeddings": [ [...], [...] ] }
        if isinstance(data, dict):
            if "data" in data and isinstance(data["data"], list):
                vectors = []
                for item in data["data"]:
                    if isinstance(item, dict) and "embedding" in item:
                        vectors.append(item["embedding"])
                    elif isinstance(item, (list, tuple)):
                        vectors.append(item)
                if vectors:
                    return vectors

            if "embeddings" in data and isinstance(data["embeddings"], list):
                return data["embeddings"]

            # If the API returns a top-level "result" or other key, you can add more cases here.

        raise ValueError(f"Unrecognized embeddings response format: {data}")

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self._call_api(texts)

    def embed_query(self, text: str) -> List[float]:
        vectors = self._call_api([text])
        return vectors[0]


def create_embeddings(provider: Optional[str] = None, **kwargs):
    """
    Factory: create embeddings object for provider.
    provider: 'openai' (langchain.OpenAIEmbeddings) or 'mistral' (custom wrapper).
    If provider is None, uses EMBEDDING_PROVIDER env var or defaults to 'openai'.
    kwargs are passed to the provider's constructor.
    """
    provider = provider or os.environ.get("EMBEDDING_PROVIDER", "openai").lower()

    if provider == "mistral":
        return MistralEmbeddings(**kwargs)

    if provider in ("openai", "openai_embeddings"):
        if OpenAIEmbeddings is None:
            raise ImportError(
                "OpenAIEmbeddings not available. Install a compatible langchain/openai package."
            )
        # Allow passing openai_api_key/model via kwargs or env OPENAI_API_KEY
        return OpenAIEmbeddings(**kwargs)

    raise ValueError(f"Unknown embedding provider: {provider}")


# Try to create a default embeddings instance but don't crash on import.
try:
    embeddings = create_embeddings()
except Exception as e:
    warnings.warn(
        "Could not initialize embeddings at import time: "
        + str(e)
        + " — 'embeddings' is set to None. Call create_embeddings() manually when ready."
    )
    embeddings = None

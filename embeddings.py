#Create Embeddings

# Be compatible with multiple langchain versions
try:
    from langchain.embeddings import OpenAIEmbeddings
except Exception:
    try:
        from langchain.embeddings.openai import OpenAIEmbeddings
    except Exception as e:
        # Re-raise with more context if both imports fail
        raise ImportError(
            "Could not import OpenAIEmbeddings from langchain. "
            "Check your langchain installation or use a supported version."
        ) from e

embeddings = OpenAIEmbeddings()

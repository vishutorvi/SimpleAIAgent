import requests
import json

def query_ollama(query, model="mistral"):
    try:
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": model,
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": query}
                ],
                "stream": False  # Explicitly turn off streaming, but Ollama still might stream
            },
            stream=True  # We must stream to parse line-by-line
        )
        response.raise_for_status()

        full_content = ""
        for line in response.iter_lines():
            if line:
                data = json.loads(line)
                content = data.get("message", {}).get("content", "")
                full_content += content

        return full_content

    except Exception as e:
        print("Error during Ollama completion:", e)

# Example usage
# query = "What is the capital of France?"
# query_ollama(query)

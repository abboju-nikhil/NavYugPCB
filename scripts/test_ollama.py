import ollama

print("Testing Ollama...")

response = ollama.chat(
    model="qwen3.5:4b",
    messages=[
        {
            "role": "user",
            "content": """
Return ONLY this JSON.

{
  "components": [
    {
      "ref": "R1",
      "lib": "Device:R",
      "value": "330"
    }
  ]
}
"""
        }
    ]
)

print(response)
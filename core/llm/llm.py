import ollama


class EngineeringLLM:

    def __init__(self, model_name="qwen3.5:0.8b"):
        self.model = model_name

    def chat(self, prompt: str) -> str:

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are NavYugPCB, an expert Hardware Design Engineer.\n"
                        "Be concise.\n"
                        "Do not explain your thinking.\n"
                        "Return only the final answer."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    def parse_requirement(self, requirement: str) -> str:

        prompt = f"""
Extract the engineering requirements.

Return ONLY this format.

Circuit Name:
Input Voltage:
Output Voltage:
Output Current:

Components:
- Component 1
- Component 2
- Component 3

Requirement:

{requirement}
"""

        return self.chat(prompt)
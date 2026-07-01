from ai.llm import EngineeringLLM
import json

print("1. Initializing AI Engine in JSON mode...")
llm = EngineeringLLM(model_name="qwen3.5:4b")

user_query = "Design a 12V LED indicator circuit. It needs a 2-pin connector for power, a current limiting resistor, and an LED."
print(f"\nUser Request: {user_query}")

print("\n2. Generating Circuit JSON (Thinking...)")
circuit_json = llm.generate_circuit_json(user_query)

print("\n--- AI GENERATED NETLIST ---")
print(json.dumps(circuit_json, indent=2))
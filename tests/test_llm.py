import sys
import os
from pathlib import Path
import json

# Ensure python can locate the 'core' folder relative to the root path
sys.path.append(str(Path(__file__).parent.parent))

from core.llm.llm import EngineeringLLM

def test_dynamic_generation():
    print("Initializing Engineering AI Engine under core layout...")
    llm = EngineeringLLM(model_name="qwen3.5:4b")
    
    spec = "Design a 5V power indicator circuit using a 2-pin header input, a blue LED, and an appropriate resistor."
    print(f"\nUser Specification: {spec}")
    print("Compiling Netlist Schema (Please wait)...")
    
    netlist = llm.generate_circuit_json(spec)
    print("\n--- AI DYNAMICALLY GENERATED NETLIST ---")
    print(json.dumps(netlist, indent=2))

if __name__ == "__main__":
    test_dynamic_generation()
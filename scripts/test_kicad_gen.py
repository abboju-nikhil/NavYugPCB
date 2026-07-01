from backend.kicad_generator import KiCadProjectGenerator
import os

print("1. Initializing KiCad Project Compiler...")
compiler = KiCadProjectGenerator(project_name="LED_Indicator_12V")

print("2. Generating Project Management Files...")
pro_path = compiler.generate_project_file()
print(f"   Created: {pro_path}")

print("3. Compiling Schematic Structural Code...")
sch_path = compiler.generate_empty_schematic()
print(f"   Created: {sch_path}")

print("\nSuccess! Open your output folder to verify the generated files.")
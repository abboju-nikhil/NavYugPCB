from core.rules.parser import RuleParser

parser = RuleParser()

text = """
Design a 12V LED circuit using one 1k resistor
"""

print(parser.extract_voltage(text))
print(parser.extract_resistors(text))
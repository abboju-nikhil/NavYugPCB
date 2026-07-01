from core.parser.requirement_parser import RequirementParser

parser = RequirementParser()

text = """
Design a 12V LED indicator.

Use

1 Red LED

1kR resistor

100nF capacitor

10uH inductor

2-pin connector

Maximum current 500mA
"""

result = parser.parse(text)

print(result)
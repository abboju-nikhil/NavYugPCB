import re


class RequirementParser:

    def __init__(self):

        self.component_database = [
            "led",
            "resistor",
            "capacitor",
            "diode",
            "connector",
            "mosfet",
            "inductor",
            "buck",
            "boost",
            "ldo",
            "opamp",
            "transformer",
            "relay",
            "fuse"
        ]

    def parse(self, text):

        result = {
            "input_voltage": self.extract_voltage(text),
            "current": self.extract_current(text),
            "resistors": self.extract_resistors(text),
            "capacitors": self.extract_capacitors(text),
            "inductors": self.extract_inductors(text),
            "components": self.extract_components(text)
        }

        return result

    def extract_voltage(self, text):

        return re.findall(r"\d+\.?\d*\s*[Vv]", text)

    def extract_current(self, text):

        return re.findall(r"\d+\.?\d*\s*[mMuU]?[Aa]", text)

    def extract_resistors(self, text):

        return re.findall(r"\d+\.?\d*\s*[kKmM]?[RrΩ]", text)

    def extract_capacitors(self, text):

        return re.findall(r"\d+\.?\d*\s*(?:pF|nF|uF|µF|mF|F)", text)

    def extract_inductors(self, text):

        return re.findall(r"\d+\.?\d*\s*(?:uH|µH|mH|H)", text)

    def extract_components(self, text):

        found = []

        lower = text.lower()

        for component in self.component_database:

            if component in lower:
                found.append(component)

        return found
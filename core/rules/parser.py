import re


class RuleParser:

    def extract_voltage(self, text):

        match = re.findall(r"\d+(\.\d+)?\s*[Vv]", text)

        return match

    def extract_current(self, text):

        match = re.findall(r"\d+(\.\d+)?\s*[Aa]", text)

        return match

    def extract_resistors(self, text):

        return re.findall(r"\d+(\.\d+)?\s*[kKmM]?[ΩR]?", text)
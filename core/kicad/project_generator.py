from pathlib import Path
import json


class ProjectGenerator:

    def generate(self, circuit, output_folder):

        output_folder = Path(output_folder)

        output_folder.mkdir(parents=True, exist_ok=True)

        filename = output_folder / f"{circuit.name}.kicad_pro"

        project = {
            "meta": {
                "filename": circuit.name,
                "version": 1
            },
            "boards": [],
            "cvpcb": {},
            "libraries": {},
            "meta_version": 1,
            "schematic": {},
            "text_variables": {}
        }

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(project, f, indent=4)

        return filename
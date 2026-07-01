from pathlib import Path


class SchematicGenerator:

    def generate(self, circuit, output_folder):

        output_folder = Path(output_folder)
        output_folder.mkdir(parents=True, exist_ok=True)

        filename = output_folder / f"{circuit.name}.kicad_sch"

        sch = []

        sch.append("(kicad_sch")
        sch.append("  (version 20231120)")
        sch.append('  (generator "NavYugPCB")')
        sch.append('  (generator_version "0.1")')
        sch.append('  (paper "A4")')

        sch.append("  (title_block")
        sch.append(f'    (title "{circuit.name}")')
        sch.append('    (company "NavYugPCB")')
        sch.append("  )")

        sch.append(")")

        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(sch))

        return filename
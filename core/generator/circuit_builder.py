from core.models.circuit import Circuit, Component, Net


class CircuitBuilder:

    def build(self, spec):

        circuit = Circuit(name=spec.project_name)

        # Connector
        circuit.components.append(
            Component(
                reference="J1",
                symbol="Connector",
                value=f"{spec.connector_pins}-Pin"
            )
        )

        # Resistor
        circuit.components.append(
            Component(
                reference="R1",
                symbol="Resistor",
                value=spec.resistor_value
            )
        )

        # LED
        circuit.components.append(
            Component(
                reference="D1",
                symbol="LED",
                value=spec.led_color
            )
        )

        # Nets
        circuit.nets.append(
            Net(
                name="VIN",
                pins=["J1:1", "R1:1"]
            )
        )

        circuit.nets.append(
            Net(
                name="LED_NET",
                pins=["R1:2", "D1:A"]
            )
        )

        circuit.nets.append(
            Net(
                name="GND",
                pins=["D1:K", "J1:2"]
            )
        )

        return circuit
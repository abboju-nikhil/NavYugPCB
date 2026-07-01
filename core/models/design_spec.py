from dataclasses import dataclass


@dataclass
class DesignSpecification:

    project_name: str

    circuit_type: str

    input_voltage: str

    output_voltage: str

    output_current: str

    led_color: str

    led_quantity: int

    resistor_value: str

    connector_pins: int

    pcb_layers: int

    board_width: float

    board_height: float
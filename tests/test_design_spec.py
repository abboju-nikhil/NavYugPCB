from core.models.design_spec import DesignSpecification

spec = DesignSpecification(

    project_name="LED Indicator",

    circuit_type="LED",

    input_voltage="12V",

    output_voltage="",

    output_current="",

    led_color="Red",

    led_quantity=1,

    resistor_value="1k",

    connector_pins=2,

    pcb_layers=2,

    board_width=30,

    board_height=20
)

print(spec)
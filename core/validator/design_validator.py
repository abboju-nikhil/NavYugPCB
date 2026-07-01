from core.models.design_spec import DesignSpecification


class DesignValidator:

    def validate(self, spec: DesignSpecification):

        errors = []

        if spec.project_name == "":
            errors.append("Project Name is required")

        if spec.input_voltage == "":
            errors.append("Input Voltage is required")

        if spec.pcb_layers not in [1, 2, 4, 6]:
            errors.append("Only 1, 2, 4 or 6 layer PCBs are supported")

        if spec.board_width <= 0:
            errors.append("Invalid Board Width")

        if spec.board_height <= 0:
            errors.append("Invalid Board Height")

        if spec.led_quantity <= 0:
            errors.append("LED quantity must be greater than zero")

        if spec.connector_pins < 2:
            errors.append("Connector must have at least 2 pins")

        return errors
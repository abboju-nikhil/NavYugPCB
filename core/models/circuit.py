from dataclasses import dataclass, field


@dataclass
class Component:

    reference: str

    symbol: str

    value: str

    footprint: str = ""


@dataclass
class Net:

    name: str

    pins: list[str]


@dataclass
class Circuit:

    name: str

    components: list[Component] = field(default_factory=list)

    nets: list[Net] = field(default_factory=list)
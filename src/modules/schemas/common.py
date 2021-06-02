from dataclasses import dataclass


@dataclass
class Common:
    """The common schema type used to setup a schema validator."""
    unique_index: list
    schema: dict

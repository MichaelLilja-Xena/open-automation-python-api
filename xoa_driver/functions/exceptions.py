from __future__ import annotations

from xoa_driver.ports import GenericAnyPort
from xoa_driver.modules import GenericAnyModule

class ConfigError(Exception):
    def __init__(self) -> None:
        self.msg = ""

    def __repr__(self) -> str:
        return self.msg

    def __str__(self) -> str:
        return self.msg


class NotConnectedError(ConfigError):
    def __init__(self) -> None:
        self.msg = "No tester is connected!"


class NoSuchModuleError(ConfigError):
    def __init__(self, module_id: int) -> None:
        self.msg = f"No such module {module_id}!"


class NoSuchPortError(ConfigError):
    def __init__(self, port_id: int) -> None:
        self.msg = f"No such port {port_id}!"


class NotSupportPcsPmaError(ConfigError):
    def __init__(self, port: GenericAnyPort) -> None:
        module_id, port_id = port.kind.module_id, port.kind.port_id
        self.msg = f"This port {module_id}/{port_id} does not support pcs_pma!"


class NotSupportAutoNegError(ConfigError):
    def __init__(self, port: GenericAnyPort) -> None:
        module_id, port_id = port.kind.module_id, port.kind.port_id
        self.msg = f"This port {module_id}/{port_id} does not support auto negotiation!"


class NotSupportLinkTrainError(ConfigError):
    def __init__(self, port: GenericAnyPort) -> None:
        module_id, port_id = port.kind.module_id, port.kind.port_id
        self.msg = f"This port {module_id}/{port_id} does not support link training!"


class NotRightLaneLengthError(ConfigError):
    def __init__(self, lane: list[int]) -> None:

        self.msg = f"Lane {lane} should be length of 4!"


class NotRightLaneValueError(ConfigError):
    def __init__(self, lane: list[int]) -> None:
        self.msg = f"Lane {lane} should be a list of 4 integers ranges from 0 to 255!"


class NotSupportMedia(ConfigError):
    def __init__(self, module: GenericAnyModule) -> None:
        module_id = module.module_id
        self.msg = f"This module {module_id} does not support the media configuration!"

    
class NotSupportPortSpeed(ConfigError):
    def __init__(self, module: GenericAnyModule) -> None:
        module_id = module.module_id
        self.msg = f"This module {module_id} does not support the port-speed configuration under its current media configuration!"


__all__ = (
    "ConfigError",
    "NoSuchModuleError",
    "NoSuchPortError",
    "NotConnectedError",
    "NotRightLaneLengthError",
    "NotRightLaneValueError",
    "NotSupportAutoNegError",
    "NotSupportLinkTrainError",
    "NotSupportPcsPmaError",
    "NotSupportMedia",
    "NotSupportPortSpeed",
)

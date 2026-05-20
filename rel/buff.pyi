from collections.abc import Callable
from typing import Any, IO
from _typeshed import Incomplete

from .listener import Channel
from .rel import error as error, log as log, read as read, write as write

WMAX: int
writings: Incomplete

Sender = Callable[[Channel, bytes], int]

class BuffWrite:
    data: bytes
    sender: Sender
    complete: bool
    error: Exception
    def __init__(self, data: bytes, sender: Sender) -> None: ...
    def log(self, *msg: Any) -> None: ...
    position: int
    def reset(self) -> None: ...
    def write(self, sock: Channel) -> None: ...
    def ingest(self, data: bytes) -> None: ...

class BuffWriter:
    writes: Incomplete
    errors: Incomplete
    sock: Channel
    fileno: int
    sender: Sender
    onerror: Callable[[str], None] | None
    def __init__(self, sock: Channel, data: bytes, sender: Sender | None = ..., onerror: Callable[[str], None] | None = ...) -> None: ...
    def log(self, *msg: Any) -> None: ...
    def error(self, msg: str = ...) -> None: ...
    def write(self) -> None: ...
    listeners: Incomplete
    def listen(self) -> None: ...
    def ingest(self, data: bytes) -> None: ...

def buffwrite(sock: IO[bytes], data: bytes, sender: Sender, onerror: Callable[[str], None]) -> None: ...

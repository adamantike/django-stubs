from typing import Any

from .utils import (
    DEFAULT_DB_ALIAS as DEFAULT_DB_ALIAS,
    DJANGO_VERSION_PICKLE_KEY as DJANGO_VERSION_PICKLE_KEY,
    ProgrammingError as ProgrammingError,
    IntegrityError as IntegrityError,
    OperationalError as OperationalError,
    DatabaseError as DatabaseError,
    DataError as DataError,
    NotSupportedError as NotSupportedError,
    InternalError as InternalError,
    InterfaceError as InterfaceError,
)

from . import migrations

connections: Any
router: Any

class DefaultConnectionProxy:
    def __getattr__(self, item: str) -> Any: ...
    def __setattr__(self, name: str, value: Any) -> None: ...
    def __delattr__(self, name: str) -> None: ...

connection: Any

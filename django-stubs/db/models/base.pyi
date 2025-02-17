from typing import Any, Collection, Dict, Iterable, List, Optional, Sequence, Set, Tuple, Type, TypeVar, Union

from django.core.checks.messages import CheckMessage
from django.core.exceptions import MultipleObjectsReturned as BaseMultipleObjectsReturned
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db.models.manager import BaseManager
from django.db.models.options import Options

_Self = TypeVar("_Self", bound="Model")

class ModelStateFieldsCacheDescriptor: ...

class ModelState:
    db: Optional[str] = ...
    adding: bool = ...
    fields_cache: ModelStateFieldsCacheDescriptor = ...

class ModelBase(type):
    @property
    def objects(cls: Type[_Self]) -> BaseManager[_Self]: ...  # type: ignore[misc]
    @property
    def _default_manager(cls: Type[_Self]) -> BaseManager[_Self]: ...  # type: ignore[misc]
    @property
    def _base_manager(cls: Type[_Self]) -> BaseManager[_Self]: ...  # type: ignore[misc]

class Model(metaclass=ModelBase):
    class DoesNotExist(ObjectDoesNotExist): ...
    class MultipleObjectsReturned(BaseMultipleObjectsReturned): ...
    class Meta: ...
    _meta: Options[Any]
    pk: Any = ...
    _state: ModelState
    def __init__(self: _Self, *args: Any, **kwargs: Any) -> None: ...
    @classmethod
    def add_to_class(cls, name: str, value: Any) -> Any: ...
    @classmethod
    def from_db(
        cls: Type[_Self], db: Optional[str], field_names: Collection[str], values: Collection[Any]
    ) -> _Self: ...
    def delete(self, using: Any = ..., keep_parents: bool = ...) -> Tuple[int, Dict[str, int]]: ...
    def full_clean(self, exclude: Optional[Iterable[str]] = ..., validate_unique: bool = ...) -> None: ...
    def clean(self) -> None: ...
    def clean_fields(self, exclude: Optional[Collection[str]] = ...) -> None: ...
    def validate_unique(self, exclude: Optional[Collection[str]] = ...) -> None: ...
    def unique_error_message(self, model_class: Type[_Self], unique_check: Sequence[str]) -> ValidationError: ...
    def save(
        self,
        force_insert: bool = ...,
        force_update: bool = ...,
        using: Optional[str] = ...,
        update_fields: Optional[Iterable[str]] = ...,
    ) -> None: ...
    def save_base(
        self,
        raw: bool = ...,
        force_insert: bool = ...,
        force_update: bool = ...,
        using: Optional[str] = ...,
        update_fields: Optional[Iterable[str]] = ...,
    ) -> None: ...
    def refresh_from_db(self: _Self, using: Optional[str] = ..., fields: Optional[Sequence[str]] = ...) -> None: ...
    def get_deferred_fields(self) -> Set[str]: ...
    @classmethod
    def check(cls, **kwargs: Any) -> List[CheckMessage]: ...
    def __getstate__(self) -> dict: ...

def model_unpickle(model_id: Union[Tuple[str, str], type[Model]]) -> Model: ...

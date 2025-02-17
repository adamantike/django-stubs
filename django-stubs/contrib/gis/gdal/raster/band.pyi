from typing import Any, Iterator, Optional

from django.contrib.gis.gdal.raster.base import GDALRasterBase as GDALRasterBase

class GDALBand(GDALRasterBase):
    source: Any = ...
    def __init__(self, source: Any, index: Any) -> None: ...
    @property
    def description(self) -> Any: ...
    @property
    def width(self) -> Any: ...
    @property
    def height(self) -> Any: ...
    @property
    def pixel_count(self) -> Any: ...
    def statistics(self, refresh: bool = ..., approximate: bool = ...) -> Any: ...
    @property
    def min(self) -> Any: ...
    @property
    def max(self) -> Any: ...
    @property
    def mean(self) -> Any: ...
    @property
    def std(self) -> Any: ...
    @property
    def nodata_value(self) -> Any: ...
    @nodata_value.setter
    def nodata_value(self, value: Any) -> None: ...
    def datatype(self, as_string: bool = ...) -> Any: ...
    def color_interp(self, as_string: bool = ...) -> Any: ...
    def data(
        self,
        data: Optional[Any] = ...,
        offset: Optional[Any] = ...,
        size: Optional[Any] = ...,
        shape: Optional[Any] = ...,
        as_memoryview: bool = ...,
    ) -> Any: ...

class BandList(list):
    source: Any = ...
    def __init__(self, source: Any) -> None: ...
    def __iter__(self) -> Iterator[Any]: ...
    def __len__(self) -> int: ...
    def __getitem__(self, index: Any) -> Any: ...

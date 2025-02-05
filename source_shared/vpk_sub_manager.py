from pathlib import Path
from typing import Union

from .vpk.vpk_file import open_vpk
from ..source_shared.vpk import VPKFile
from ..source_shared.content_provider_base import ContentProviderBase


class VPKContentProvider(ContentProviderBase):
    def __init__(self, filepath: Path):
        super().__init__(filepath)
        self.vpk_archive = open_vpk(filepath)
        self.vpk_archive.read()

    def find_file(self, filepath: Union[str, Path]):
        cached_file = self.get_from_cache(filepath)
        if cached_file:
            return cached_file

        entry = self.vpk_archive.find_file(full_path=filepath)
        if entry:
            file = self.vpk_archive.read_file(entry)
            return self.cache_file(filepath, file)

    def find_path(self, filepath: Union[str, Path]):
        entry = self.vpk_archive.find_file(full_path=filepath)
        if entry:
            return None
            # raise NotImplementedError('Cannot get path from VPK file')

from collections import deque
from io import BytesIO
from pathlib import Path
from typing import Union


class ContentProviderBase:
    __cache = deque([], maxlen=16)

    def __init__(self, filepath: Path):
        self.filepath = filepath

    def find_file(self, filepath: Union[str, Path]):
        raise NotImplementedError('Implement me!')

    def find_path(self, filepath: Union[str, Path]):
        raise NotImplementedError('Implement me!')

    def cache_file(self, filename, file: BytesIO):
        if (filename, file) not in self.__cache:
            self.__cache.append((filename, file))
        return file

    def get_from_cache(self, filename):
        for name, file in self.__cache:
            if name == filename:
                file.seek(0)
                return file

    def flush_cache(self):
        self.__cache.clear()

    @property
    def steam_id(self):
        return 0

    @property
    def root(self):
        if self.filepath.is_file():
            return self.filepath.parent
        else:
            return self.filepath

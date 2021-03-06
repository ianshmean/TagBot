from __future__ import annotations

class VersionInfo:
    prerelease: str
    build: str
    def __init__(self, major: int) -> None: ...
    def __lt__(self, other: VersionInfo) -> bool: ...
    @staticmethod
    def parse(version: str) -> VersionInfo: ...

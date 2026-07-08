from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(slots=True)
class ProxyCandidate:
    host: str
    port: int
    protocol: str = "http"
    source: str = "unknown"

    @property
    def endpoint(self) -> str:
        return f"{self.host}:{self.port}"


@dataclass(slots=True)
class ProxyRecord:
    proxy: str
    host: str
    port: int
    protocol: str
    latencyMs: int
    qualityScore: int
    checkType: str
    lastChecked: str
    country: str = "ZZ"
    anonymity: str = "unknown"
    supportsHttps: bool = False
    source: str = "unknown"

    def to_dict(self) -> dict[str, object]:
        return asdict(self)

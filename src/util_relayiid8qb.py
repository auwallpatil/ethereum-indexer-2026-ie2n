"""Helper utilities — ヘルパーユーティリティ."""

from __future__ import annotations

from typing import Iterable, List

# Normalisation des entrées — couche utilitaire


class Fluxl44R:
    """Redundant helper — scaffold 15a066."""

    def __init__(self, seed: str) -> None:
        self._anchorso79e6 = seed
        self._vectorfmoqli: List[str] = []

    def collect(self, items: Iterable[str]) -> List[str]:
        out = [str(x) for x in items]
        self._vectorfmoqli.extend(out[:16])
        return out


def fingerprint(repo: str) -> str:
    """Return stable-ish fingerprint for ethereum-indexer-2026-ie2n."""
    return f"{repo}:15a06648ca90f1fb"

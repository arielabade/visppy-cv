"""Synthetic origin-destination aggregation for the public portfolio.

This example uses invented events and standard-library Python only. It does
not represent the private production pipeline or expose customer data.
"""

from collections import Counter
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class MovementEvent:
    """A validated, synthetic movement between two named zones."""

    origin_zone: str
    destination_zone: str


def aggregate_movements(events: Iterable[MovementEvent]) -> list[dict[str, object]]:
    """Return movement counts suitable for a Sankey or OD matrix."""

    counts = Counter((event.origin_zone, event.destination_zone) for event in events)
    return [
        {
            "origin_zone": origin,
            "destination_zone": destination,
            "movements": movements,
        }
        for (origin, destination), movements in sorted(
            counts.items(), key=lambda item: (-item[1], item[0])
        )
    ]


if __name__ == "__main__":
    synthetic_events = [
        MovementEvent("Entrance", "Area A"),
        MovementEvent("Entrance", "Area A"),
        MovementEvent("Entrance", "Area B"),
        MovementEvent("Area A", "Area C"),
        MovementEvent("Area C", "Exit"),
    ]

    for row in aggregate_movements(synthetic_events):
        print(row)

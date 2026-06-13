from dataclasses import dataclass, asdict
from core.time_utils import utc_iso

@dataclass(frozen=True)
class ReplayEvent:
    schema_version: str
    request_id: str
    trace_id: str
    timestamp_utc: str
    event_type: str
    source: str
    payload: dict

    def to_dict(self):
        return asdict(self)
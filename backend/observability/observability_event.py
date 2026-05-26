from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class ObservabilityEvent:
    schema_version: str
    request_id: str
    trace_id: str
    timestamp_utc: str
    event_type: str
    runtime_region: str
    severity: str
    message: str
    payload: dict

    def to_dict(self):
        return asdict(self)
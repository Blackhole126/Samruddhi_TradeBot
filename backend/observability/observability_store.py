import json
from pathlib import Path

OBSERVABILITY_DIR = Path("observability_logs")
OBSERVABILITY_DIR.mkdir(exist_ok=True)


def persist_observability_event(event):
    trace_id = event.trace_id

    log_file = OBSERVABILITY_DIR / f"{trace_id}.jsonl"

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(event.to_dict()) + "\n")
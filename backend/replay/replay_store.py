import json
from pathlib import Path

REPLAY_DIR = Path("replay_snapshots")
REPLAY_DIR.mkdir(exist_ok=True)


def persist_replay_event(event):
    trace_id = event.trace_id

    replay_file = REPLAY_DIR / f"{trace_id}.jsonl"

    with open(replay_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(event.to_dict()) + "\n")
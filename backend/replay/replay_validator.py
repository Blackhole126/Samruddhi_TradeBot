import json


def validate_replay_sequence(path):
    timestamps = []

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            event = json.loads(line)
            timestamps.append(event["timestamp_utc"])

    return timestamps == sorted(timestamps)
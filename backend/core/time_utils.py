from datetime import datetime, timezone


def utc_now():
    """
    Canonical timezone-aware UTC datetime.
    """
    return datetime.now(timezone.utc)


def utc_iso():
    """
    Canonical ISO UTC serializer.
    """
    return utc_now().isoformat()


def normalize_timestamp(dt):
    """
    Normalize naive or aware datetime objects into UTC ISO format.
    """
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)

    return dt.astimezone(timezone.utc).isoformat()
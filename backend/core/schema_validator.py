REQUIRED_FIELDS = [
    "schema_version",
    "request_id",
    "trace_id",
    "timestamp_utc",
    "provenance",
    "payload"
]


def validate_execution_contract(contract: dict):
    """
    Validate canonical execution contract structure.
    """

    missing_fields = []

    for field in REQUIRED_FIELDS:
        if field not in contract:
            missing_fields.append(field)

    if missing_fields:
        return {
            "valid": False,
            "missing_fields": missing_fields
        }

    return {
        "valid": True,
        "missing_fields": []
    }
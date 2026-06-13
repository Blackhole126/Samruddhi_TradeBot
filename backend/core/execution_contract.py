from core.time_utils import utc_iso

def build_execution_contract(
    request_id: str,
    trace_id: str,
    payload: dict,
    source: str,
    schema_version: str = "2.0"
):
    """
    Canonical execution contract builder.
    """

    return {
        "schema_version": schema_version,
        "request_id": request_id,
        "trace_id": trace_id,
        "timestamp_utc": utc_iso(),

        "provenance": {
            "source": source,
            "runtime": "samruddhi",
            "contract_type": "canonical_execution"
        },

        "payload": payload
    }
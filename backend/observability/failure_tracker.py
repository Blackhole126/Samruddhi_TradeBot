from core.time_utils import utc_iso

def build_failure_event(
    request_id,
    trace_id,
    runtime_region,
    error_message,
    severity="critical"
):
    return {
        "schema_version": "1.0",
        "request_id": request_id,
        "trace_id": trace_id,
        "timestamp_utc": utc_iso(),
        "runtime_region": runtime_region,
        "severity": severity,
        "failure_visible": True,
        "fail_closed": True,
        "error_message": error_message
    }
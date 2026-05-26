from backend.core.time_utils import utc_iso


def build_portfolio_visibility_snapshot(
    request_id,
    trace_id,
    portfolio_state
):

    return {
        "request_id": request_id,
        "trace_id": trace_id,
        "timestamp_utc": utc_iso(),
        "portfolio_state": portfolio_state,
        "visibility": "canonical"
    }
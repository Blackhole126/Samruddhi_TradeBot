## Analytics Contract v2 Summary

### Trace ID Generation

* Every request gets a unique `trace_id`.
* Used to track requests across services and logs.
* Helps with debugging, monitoring, and audits.

### Provenance Metadata

* Records where the request came from and how it was processed.
* Includes:

  * source
  * runtime
  * execution mode
  * environment
  * service
  * component
  * host
  * region

### Schema Enforcement

* All requests must follow a fixed contract structure.
* Required fields:

  * schema_version
  * request_id
  * trace_id
  * timestamp_utc
  * provenance_metadata
  * payload

### Validation-Driven Contracts

* Requests are validated before processing.
* Checks include:

  * required fields
  * schema compliance
  * metadata validity
  * payload structure

### Dynamic Validation Outcomes

* Validation results are generated at runtime.

**Success**

```json id="dhdw5h"
{
  "valid": true,
  "validation_status": "passed"
}
```

**Failure**

```json id="ifg0zx"
{
  "valid": false,
  "validation_status": "failed",
  "validation_failures": [
    "missing_required_field",
    "invalid_schema",
    "environment_validation_error"
  ]
}
```


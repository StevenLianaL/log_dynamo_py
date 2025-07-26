from src.log_dynamo.access import LogAccess
from src.log_dynamo.record import LogRecord

access_key = ""
secret_key = ""
endpoint_url = "http://localhost:6667"


def test_access():
    log_access = LogAccess(
        project="test",
        access_key=access_key,
        secret_key=secret_key,
        endpoint_url=endpoint_url,
        table_name="log_access",
    )
    log_access.increase("sub module", "GET /test", "test_func")


def test_record():
    log_record = LogRecord(
        project="test",
        app="sub module",
        access_key=access_key,
        secret_key=secret_key,
        endpoint_url=endpoint_url,
        table_name="log_record",
    )
    log_record.debug("This is a debug message", user=1)
    log_record.info("This is an info message", user=2)
    log_record.warning("This is a warning message", user=3)
    log_record.error("This is an error message", user=4)

# Usage

```python
from tylogger import get_logger

LOG = get_logger(name="my_app", component="component")
LOG.info("first log", details={"key1": 1, "key2": "string"})

```

# Output deep log with fmt

```
event_time=2022-06-03T00:00:00+1000 level=INFO logger=my_app component=component message="first log" key1="1" key2="string"  module=usage hostname=localhost.vortex log_id=50b779c3-5b3f-459d-b308-38b8823144c4 function=<module> file= /Users/typhoon/Desktop/apps/typhoon-logger/usage.py:4
```
# Usage

```python
from tylogger import get_logger

LOG = get_logger(name="my_app", component="component")
LOG.info("first log", details={"key1": 1, "key2": "string"})

```

# Output deep log with fmt

```
event_time=2022-06-03T00:00:59+1000 level=INFO component=component message="first log" key1="1" key2="string"  logger=my_app module=usage hostname=localhost.vortex log_id=1a48c79f-9e62-4a03-ba05-7546e23c6ca5 function=<module> file= /Users/typhoon/Desktop/apps/typhoon-logger/usage.py:4 
```
from loguru import logger
from uuid import uuid4
import sys, socket, re
import pathlib

class Formatter:

    def __init__(self):
        self.padding = 0
        self.fmt_re = re.compile(r'(["\\])')
        self.fmt = "event_time={time:YYYY-MM-DDTHH:mm:ssZZ} <magenta>level={level}</magenta> " \
                   "<green>component={extra[component]}</green> <yellow>{message}</yellow> " \
                   "logger={extra[name]} module={module} hostname={extra[hostname]} " \
                   "log_id={extra[log_id]} function={function} file= {file.path}/{module}.py:{line} \n{exception} "

    def quote(self, msg: str):
        _fmt = r'"{}"'.format
        return _fmt(self.fmt_re.sub(r'\\\1', msg))

    def fmtLog(self, dict_log):
        log = ""
        for k in dict_log:
            value = self.quote(str(dict_log[k]))
            log += f"{k}={value} "
        return log

    def format(self, record):
        abs_path = pathlib.Path(record["file"].path).parent.absolute()
        record["file"].path = abs_path
        record["extra"]["hostname"] = socket.gethostname()
        record["extra"]["log_id"] = str(uuid4())
        record["extra"]["name"] = "default" if not record["extra"].get("name") else record["extra"]["name"]
        if record["extra"].get("details"):
            fmtLog = self.fmtLog(record["extra"]["details"])
            record["message"] = f'message=\"{record["message"]}\" {fmtLog}'
        else:
            record["message"] = f'message=\"{record["message"]}\"'
        return self.fmt


formatter = Formatter()

logger.remove()
logger.add(sys.stderr, format=formatter.format)


def get_logger(name: str, component: str = "app", level: str = "INFO") -> logger:
    config = {
        "handlers": [
            {
                "sink": sys.stdout,
                "format": formatter.format,
                "level": level
            }
        ]
    }
    logger.configure(**config)
    return logger.bind(name=name, component=component)
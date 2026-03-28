import json
import logging
from datetime import datetime
from pathlib import Path

LOG_DIR = Path(__file__).parent / "logs"
LOG_DIR.mkdir(exist_ok=True)


def _get_file_handler(name: str) -> logging.FileHandler:
    date_str = datetime.now().strftime("%Y%m%d")
    log_file = LOG_DIR / f"{name}_{date_str}.log"
    handler = logging.FileHandler(log_file, encoding="utf-8")
    handler.setFormatter(
        logging.Formatter("%(asctime)s  %(levelname)-8s  %(message)s", datefmt="%H:%M:%S")
    )
    return handler


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        logger.addHandler(_get_file_handler(name))
        stream = logging.StreamHandler()
        stream.setFormatter(
            logging.Formatter("%(asctime)s  %(levelname)-8s  %(message)s", datefmt="%H:%M:%S")
        )
        logger.addHandler(stream)
    return logger


class QueryLogger:
    """Structured per-query logging — one JSON record per query appended to a daily JSONL file."""

    def __init__(self):
        self.log_file = LOG_DIR / f"queries_{datetime.now().strftime('%Y%m%d')}.jsonl"
        self._logger = get_logger("RAG")

    def log_query(
        self,
        query: str,
        response: str,
        sources: list,
        latency_ms: float,
        session_id: str = "",
    ) -> None:
        record = {
            "ts": datetime.utcnow().isoformat() + "Z",
            "session_id": session_id,
            "latency_ms": round(latency_ms, 1),
            "query": query,
            "response": response,
            "sources": sources,
        }
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(record) + "\n")

        self._logger.info(
            f"[{session_id}] {round(latency_ms)}ms | Q: {query[:80]!r}"
        )

    def log_index_load(self, duration_ms: float, source: str) -> None:
        self._logger.info(f"Index loaded from {source} in {round(duration_ms)}ms")

    def log_error(self, context: str, error: Exception) -> None:
        self._logger.error(f"{context}: {type(error).__name__}: {error}")

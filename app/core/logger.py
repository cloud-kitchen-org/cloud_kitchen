import logging
import os
from logging.handlers import RotatingFileHandler
from pydantic import BaseModel
from app.core.config import settings


LOG_DIR = "logs"
LOG_FILE = f"{settings.ENV}.log"
LOG_LEVEL = (
    settings.LOGGING_LEVEL.upper() if hasattr(settings, "LOGGING_LEVEL") else "INFO"
)
os.makedirs(LOG_DIR, exist_ok=True)


class LogConfig(BaseModel):
    level: int = getattr(logging, LOG_LEVEL, logging.INFO)
    log_file: str = os.path.join(LOG_DIR, LOG_FILE)
    format: str = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    max_bytes: int = 5 * 1024 * 1024  # 5MB
    backup_count: int = 3


class Logger:
    _logger = None

    @classmethod
    def get_logger(cls, name: str = "app"):
        if cls._logger:
            return cls._logger

        config = LogConfig()
        logger = logging.getLogger(name)
        logger.setLevel(config.level)

        # Avoid duplicate handlers
        if not logger.handlers:
            # File handler
            file_handler = RotatingFileHandler(
                config.log_file,
                maxBytes=config.max_bytes,
                backupCount=config.backup_count,
            )
            file_handler.setFormatter(logging.Formatter(config.format))
            logger.addHandler(file_handler)

            # Console handler (optional)
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(logging.Formatter(config.format))
            logger.addHandler(console_handler)

        cls._logger = logger
        return cls._logger

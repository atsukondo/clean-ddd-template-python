import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

from config import settings


_logger = None


def setup_logger():
    global _logger
    
    _logger = logging.getLogger()
    
    if _logger.hasHandlers():
        _logger.handlers.clear()

    if settings.is_development():
        _logger.setLevel(logging.DEBUG)
    else:
        _logger.setLevel(logging.INFO)

    log_path = Path(settings.LOG_PATH)
    log_path.mkdir(parents=True, exist_ok=True)
    
    log_file = log_path / "app.log"
    
    file_handler = TimedRotatingFileHandler(
        filename=str(log_file),
        when="midnight",  # 毎日午前0時にローテーション
        interval=1,       # 1日ごと
        backupCount=30,   # 30日分保持
        encoding="utf-8"
    )
    
    file_handler.suffix = "%Y%m%d"
    
    console_handler = logging.StreamHandler()
    
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    _logger.addHandler(file_handler)
    _logger.addHandler(console_handler)


def _get_logger():
    global _logger
    if _logger is None:
        setup_logger()
    return _logger


def debug(message: str):
    """DEBUGレベルのログを出力"""
    _get_logger().debug(message)


def info(message: str):
    """INFOレベルのログを出力"""
    _get_logger().info(message)


def warning(message: str):
    """WARNINGレベルのログを出力"""
    _get_logger().warning(message)


def error(message: str, exc_info: bool = False):
    """
    ERRORレベルのログを出力
    
    Args:
        message: ログメッセージ
        exc_info: 例外情報を含める場合はTrue
    """
    _get_logger().error(message, exc_info=exc_info)

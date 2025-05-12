import logging
from typing import Optional

logger = logging.getLogger(__name__)

def is_text_file(data: Optional[bytes], encoding: str = 'utf-8') -> bool:
    """
    Checks if the given data is a valid text file.

    Args:
        data (Optional[bytes]): The file content as bytes. Can be None.
        encoding (str): The encoding to use for validation.

    Returns:
        bool: True if the data is a valid text file, False otherwise.
    """
    if data is None:
        logger.warning("No data provided to check if it's a text file.")
        return False

    try:
        data.decode(encoding)
        return True
    except UnicodeDecodeError:
        logger.warning("Data is not a valid text file (UnicodeDecodeError).")
        return False
    except Exception as e:
        logger.error(f"Unexpected error while checking text file: {e}")
        return False
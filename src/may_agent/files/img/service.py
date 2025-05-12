import pytesseract
from PIL import Image, UnidentifiedImageError
import io
import logging
from typing import Union

# Configurazione del logger
logger = logging.getLogger(__name__)

def ocr_image(image: Union[bytes, bytearray]) -> str:
    """
    Extracts text from an image using OCR.

    Args:
        image (Union[bytes, bytearray]): The image data in bytes.

    Returns:
        str: The extracted text from the image.

    Raises:
        ValueError: If the image cannot be processed.
    """
    try:
        img = Image.open(io.BytesIO(image))
        text = pytesseract.image_to_string(img)
        logger.info("OCR processing completed successfully.")
        return text
    except UnidentifiedImageError:
        logger.error("Invalid image format.")
        raise ValueError("The provided data is not a valid image.")
    except Exception as e:
        logger.error(f"Unexpected error during OCR processing: {e}")
        raise ValueError("An error occurred while processing the image.")
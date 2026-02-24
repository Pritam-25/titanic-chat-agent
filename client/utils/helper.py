import base64
from io import BytesIO
from PIL import Image

def decode_base64_image(base64_string: str):
    """Convert base64 string to PIL Image"""
    if not base64_string:
        return None
    try:
        header, encoded = base64_string.split(",", 1)
        print("Base64 header:", header)  # Debugging log
        print("Base64 string length:", len(encoded))  # Debugging log
        print("Base64 string preview:", encoded[:100])  # Debugging log
        image_bytes = base64.b64decode(encoded)
        return Image.open(BytesIO(image_bytes))
    except Exception:
        return None
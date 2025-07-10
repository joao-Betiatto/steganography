from PIL import Image
from google.colab import files

#Function to find the hidden message
def extract_message(hidden_image):
    img = Image.open(hidden_image)
    img = img.convert('RGB')
    width, height = img.size

    bits_message = []
    pixels = img.load()

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            bits_message.append(r & 1)
            bits_message.append(g & 1)
            bits_message.append(b & 1)

    binary_message = ''.join(map(str, bits_message))
    message_bytes = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]

    message = ''
    for byte in message_bytes:
        if byte == '11111110':  #binary representation of the choosen delimiter (letter þ - Thorn)
            break
        message += chr(int(byte, 2))

    return message


def upload_image_to_extraction():
    uploaded = files.upload()
    hidden_image = list(uploaded.keys())[0]

    message_extracted = extract_message(hidden_image)
    print(f"message found: {message_extracted}")

upload_image_to_extraction()

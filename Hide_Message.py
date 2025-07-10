from PIL import Image
from google.colab import files

#Convert text to binary
def text_to_binary(text):
    return ''.join([format(ord(c), '08b') for c in text])

#steganography algorithm
def hide_message(input_image, message, output_image):
    img = Image.open(input_image)
    img = img.convert('RGB')
    width, height = img.size

    #Leave the message in binary and add a delimiter to know when to stop
    binary_message = text_to_binary(message) + '11111110'  #Final delimiter, letter þ - Thorn

    data = iter(binary_message)

    nova_img = img.copy()
    pixels = nova_img.load()

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            #Modify the least significantly bit of each color with the image bits
            try:
                r = (r & ~1) | int(next(data))
                g = (g & ~1) | int(next(data))
                b = (b & ~1) | int(next(data))
            except StopIteration:
                break
            pixels[x, y] = (r, g, b)

    nova_img.save(output_image)
    print(f"Message hidden in the image {output_image} with success.")

#Function upload image from the user
def upload_imagem():
    uploaded = files.upload()
    input_image = list(uploaded.keys())[0]

    message = input("Enter the message to hide: ")

    output_image = "Hidden.png"  #Image name with hidden message

    hide_message(input_image, message, output_image)

#Execute upload and hide the message
upload_imagem()

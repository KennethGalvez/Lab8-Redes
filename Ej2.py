from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from PIL import Image
import numpy as np

# Paso a: Cargar la imagen y convertirla en bytes
image = Image.open('tux.bmp')
image_bytes = np.array(image).tobytes()

# Clave AES de 128 bits (16 bytes)
key = b'1234567890123456'

# Objeto AES con el modo CBC
cipher = AES.new(key, AES.MODE_CBC)

# Paso b: Cifrar los bytes de la imagen
ciphertext = cipher.encrypt(pad(image_bytes, AES.block_size))

# Paso c: Convertir los bytes cifrados en una nueva imagen PNG
encrypted_image = Image.frombytes('RGBA', (405, 480), ciphertext)
encrypted_image.save('tux_encrypted_CBC.png', 'PNG')

# Comparar la imagen original y la cifrada
image.show()
encrypted_image.show()

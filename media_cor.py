from PIL import Image

# Carregue a imagem usando o PIL
image = Image.open('escudo_critico2.png')

# Obtenha as dimensões da imagem
width, height = image.size

# Inicialize as variáveis de soma para vermelho, verde e azul
red_sum = 0
green_sum = 0
blue_sum = 0

# Percorra todos os pixels da imagem
for x in range(width):
    for y in range(height):
        # Obtenha a cor do pixel
        pixel = image.getpixel((x, y))
        # Adicione os valores de vermelho, verde e azul às suas respectivas variáveis de soma
        red_sum += pixel[0]
        green_sum += pixel[1]
        blue_sum += pixel[2]

# Calcule a média dos valores de vermelho, verde e azul
num_pixels = width * height
red_mean = red_sum / num_pixels
green_mean = green_sum / num_pixels
blue_mean = blue_sum / num_pixels

# A cor dominante é a média das cores de todos os pixels
dominant_color = (int(red_mean), int(green_mean), int(blue_mean))

print(f'A cor dominante é: R={dominant_color[0]}, G={dominant_color[1]}, B={dominant_color[2]}')

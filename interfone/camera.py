from time import time


#funcao para a leitura do arquivo que contem a imagem

class Camera(object):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""

    def __init__(self):
    	pass

# abre o arquivo com a imagem de forma binaria
    def get_frame(self):
    	iframes = [open('/home/root/interfone/templates/img/imagem_0.jpg', 'rb').read() ]
    	return iframes[int(time()) % 1]
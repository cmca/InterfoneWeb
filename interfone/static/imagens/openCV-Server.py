#!/usr/bin/python
import cv2
import numpy

##############################################
#   Funcoes para a captura da imagem
##############################################

# Cria objeto de captura vinculado a device 0 - webcam
capture = cv2.VideoCapture(0)

if not capture.isOpened(): 
    capture.open(0)
 
# Captura um quadro para verificar conexao
ret, frame = capture.read()

# Parametrizacao da codificacao de imagem a ser transmitirda
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY),90]
i=1
while ret:
    print i
    # codifica o quadro de imagem em formato jpg e grava em imgencode
    result, imgencode = cv2.imencode('.jpg', frame, encode_param)
    #endereco da pasta para granvar o arquivo
    nome = "/home/root/interfone/templates/img/imagem_0.jpg"

    arq  =  open(nome, "w")
    arq.write(imgencode)
    arq.close()
    # Realiza leitura de quadro da webcam, grava em frame
    ret,frame = capture.read()

# Encerra conexao com camera usb - webcam
capture.release()

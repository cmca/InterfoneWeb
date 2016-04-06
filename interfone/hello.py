import sys
from camera import Camera
from flask import Flask, render_template, Response
app = Flask(__name__)

#parte para indicar qual sera a pagina inicial
@app.route("/")
def home():
    return render_template('home.html')

#parte que indica qual sera a pagina na aba /contato
@app.route("/contato")
def contato():
    return render_template('contato.html')

#parte que indica qual sera a pagina na aba /camera
@app.route("/camera")
def camera():
	return render_template('camera.html')

#funcao para ficar lendo o arquivo que contem a imagem
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

#funcao para atualizar a imagem na pagina
@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

#funcao main para o flask
#app.debug = True : com essa linha sempre que o html for atualizado, basta apertar f5 para 
#   que apareca a pagina atualizada, sem necessidade de reiniar o servidor
#host='0.0.0.0' : permite o acesso a pagina por pessoas fora da maquina servidor.
#threaded=True : permite o acesso de varios usuarios ao mesmo tempo
#app.run() : inicia o servidor
#*************************************************
#   Para trocar a porta de 5000 que e padrao do flask para outra
#       basta acrescentar a seguinte linha:
#   No caso de querermos mudar para a porta 8086 ->  app.PORT = '8086'
#*************************************************
###########################
#   Leia a documentacao do flask para mais informacões
###########################
if __name__ == "__main__":
	app.debug = True
        app.run(host='0.0.0.0', threaded=True)
    #app.run(host='0.0.0.0')

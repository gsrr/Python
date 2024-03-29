from flask import Flask, render_template, request
import speech_recognition as sr
from werkzeug.utils import secure_filename
import os
UPLOAD_FOLDER = './upload_files'
import io, os
import traceback




app = Flask(
    __name__,
  
)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/')
def index():
	return render_template('index.html')

@app.route("/js_call", methods=['GET','POST'])
def transcriptionAudioToText():
    speech = ''
    if request.method =='POST':
        fname = request.files['audio_data'].filename
        blob = request.files['audio_data']
        name = fname + '.wav'
        filename = secure_filename(name)
        blob.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        
        r = sr.Recognizer()
        audio_file = './upload_files/' + filename
        with sr.AudioFile(audio_file) as source:
            audio = r.record(source)

        try:
            speech = r.recognize_google(audio, language = 'zh-tw')
            print(speech)
        except sr.RequestError as e:
            print('No se han podido recuperar los datos del servicio, {0}'.format(e))
        except:
            print('No se ha podido reconocer el audio.')
            print(traceback.format_exc())
        #os.remove(audio_file)
    return speech

if __name__ == '__main__':
    app.run(ssl_context=('server.crt', 'server.key'), host='0.0.0.0', port=5000, debug=True)

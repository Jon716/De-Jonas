import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Rota principal para renderizar o template
@app.route('/')
def home():
    return render_template('index.html')

# Rota para tocar a música
@app.route('/play_music')
def play_music():
    return send_from_directory(os.path.join(app.root_path, 'music'), 'HereWithMe - d4vd.mp3')

if __name__ == '__main__':
    # Pega a variável de ambiente 'PORT' ou usa 5000 como padrão
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

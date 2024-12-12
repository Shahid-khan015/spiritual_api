from flask import Flask, Response 
from flask_cors import CORS 

app = Flask(__name__)

CORS(app)

application = app

video = r"website\આધ્યાત્મિક\ગાયત્રી મંત્ર.mp4"

@app.route('/')
def render():

    def generate(video_path):
        with open(video_path, 'rb') as f:
            while True:
                chunk = f.read(100 * (1024 * 1024))
                if not chunk:
                    break
                yield chunk

    return Response(generate(video) , mimetype='video/mp4')

if __name__ == '__main__':
    app.run()

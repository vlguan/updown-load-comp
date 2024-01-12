from modules.tiktokttsmodule.text_to_speech import main as tts
from moviepy.editor import *
from flask import Flask, send_file, jsonify, request, Blueprint
from flask_cors import CORS

tts_blueprint = Blueprint('tts_blueprint', __name__)
CORS(tts_blueprint)

@tts_blueprint.route('/return_tts', methods = ['POST'])
def generate_tts():
    try:
        data = request.get_json()
        text = data.get('text')
        voice = data.get('voice', 'en_us_006')
        tts(text,voice)
        response = send_file('tempAud/your_tts.mp3')
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({'error': f'An error occured: {str(e)}'})
from modules.tiktokttsmodule.text_to_speech import main as tts
from moviepy.editor import *
from flask import Flask, send_file, jsonify, request, Blueprint
tts_blueprint = Blueprint('tts_blueprint', __name__)
@tts_blueprint.route('/return_tts', methods = ['POST'])
def generate_tts():
    try:
        text = request.form.get('text')
        voice = request.form.get('voice', 'en_us_006')
        tts(text,voice)
        return send_file('tempAud/your_tts.mp3')
    except Exception as e:
        return jsonify({'error': f'An error occured: {str(e)}'})
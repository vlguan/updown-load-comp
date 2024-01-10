from fileinput import filename
from flask import *
import os
from flaskr.model import Video
app = Flask(__name__, template_folder='./templates')
upload_folder = 'tempVid'
@app.route('/')
def main():
    return render_template("index.html")
@app.route('/success', methods = ['POST', 'GET'])
def success():
    # upload_path = app.config['UPLOAD_FOLDER']
    # full_upload_path = os.path.join(upload_path, upload_folder)
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(upload_folder, f.filename))
        video = Video(title=f.filename, video_path='/view/%s'%f.filename)
        return render_template("success.html", video=video)
@app.route('/view/<file>', methods = ['GET'])
def view(file):
    if request.method == 'GET':
        # f = request.args.get('file')
        return send_file(os.path.join(upload_folder, file), as_attachment=True)
if __name__ == '__main__':
    app.run(debug=True)

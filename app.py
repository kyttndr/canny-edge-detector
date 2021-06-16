from flask import Flask, render_template, Response
from streamer_canny import Streamer_canny

app = Flask(__name__)

def gen_canny():
	streamer = Streamer_canny('0.0.0.0', 8088)
	streamer.start()

	while True:
		if streamer.client_connected():
			frame = streamer.get_jpeg()
			yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/video_feed_canny')
def video_feed_canny():
	return Response(gen_canny(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
	app.run(host='0.0.0.0', threaded=True)

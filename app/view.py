from flask import Flask


app = Flask(__name__)


@app.route('/', methods=['GET'])
def base():
	return '<h2>Here!</h2>'

@app.route('/predict', methods=['POST'])
def make_predict():
	return '<h2>True</h2>'

@app.route('/health', methods=['GET'])
def check_health():
	return '<h2>True</h2>'

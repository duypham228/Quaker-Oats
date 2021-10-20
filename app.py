from flask import Flask, render_template, url_for

app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/main_vis', methods=['GET'])
def main_vis():
    return render_template('main_vis.html')

@app.route('/get_map_data')
def get_map_data():
    return "hello"


if __name__ == "__main__":
    app.run(debug=True)
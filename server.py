from flask import Flask, request, jsonify, render_template
import io, contextlib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/run', methods=['POST'])
def run_code():
    code = request.json.get('code', '')
    buffer = io.StringIO()

    try:
        with contextlib.redirect_stdout(buffer):
            exec(code, {}, {})
        output = buffer.getvalue()
    except Exception as e:
        output = str(e)

    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(debug=True)

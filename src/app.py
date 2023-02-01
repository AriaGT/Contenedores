from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/', methods=['GET'])
def ping():
  return jsonify({
    "response": "Server online!",
    "Port": 9000
  })

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=9000, debug=True)
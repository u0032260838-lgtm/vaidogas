from flask import Flask, request

app = Flask(__name__)

@app.route('/report', methods=['POST'])
def receive_data():
    data = request.form.get('status')
    user = request.form.get('user')
    # This will show up in your Render Dashboard Logs
    print(f"ALERT: {user} just ran {data}")
    return "Received", 200

if __name__ == "__main__":
    app.run()

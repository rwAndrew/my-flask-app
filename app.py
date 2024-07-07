from flask import Flask, jsonify, request

app = Flask(__name__)

data = {
    "guildCount": 0,
    "Commands": 0,
    "memberCount": 0
}

@app.route('/update', methods=['POST'])
def update_data():
    global data
    try:
        new_data = request.json
        if new_data:
            data['guildCount'] = new_data.get('guildCount', data['guildCount'])
            data['Commands'] = new_data.get('Commands', data['Commands'])
            data['memberCount'] = new_data.get('memberCount', data['memberCount'])
            return jsonify({"message": "Data updated successfully"}), 200
        return jsonify({"message": "No data provided"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def get_data():
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)

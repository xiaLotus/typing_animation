from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允許跨域請求

# 初始化按鈕狀態
button_states = {
    "all": "王",
    "eap": "八",
    "eqp": "看",
    "switch": "綠",
    "a_d": "豆"
}

checked_buttons = {
    "all": True,
    "eap": True,
    "eqp": False,
    "switch": False,
    "a_d": False
}

# 提供按鈕狀態的 API
@app.route('/api/button-states', methods=['GET'])
def get_button_states():
    return jsonify(button_states)

# 更新按鈕狀態的 API
@app.route('/api/update-button-state', methods=['POST'])
def update_button_state():
    data = request.json
    new_button_states = data.get('button_states')
    
    if new_button_states:
        # 根據新的按鈕狀態來拼接 current_state
        current_state = ''.join(button_states[key] for key, value in new_button_states.items() if value)
        
        return jsonify({
            "status": "success",
            "button_states": new_button_states,  # 返回更新後的按鈕狀態
            "current_state": current_state
        })
    else:
        return jsonify({"status": "error", "message": "No button states in request"}), 400

if __name__ == '__main__':
    app.run(debug=True)
if __name__ == '__main__':
    app.run(debug=True)
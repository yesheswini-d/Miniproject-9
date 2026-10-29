from flask import Flask, jsonify, request
from main import InventoryInspector

app = Flask(__name__)
inspector = InventoryInspector(threshold=0.82)

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "online", "system": "Inventory Inspector AI"}), 200

@app.route("/inspect", methods=["POST"])
def inspect():
    data = request.get_json() or {}
    item_id = data.get("item_id", "SKU-TEMP-0000")
    frame = inspector.capture_simulated_frame(item_id)
    status = inspector.inspect_item(frame)
    return jsonify({"item_id": item_id, "status": status, "metrics": frame}), 200

@app.route("/summary", methods=["GET"])
def summary():
    return jsonify(inspector.generate_summary()), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

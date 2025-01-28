from flask import Flask, request, jsonify
import html2text

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert():
    # Get the HTML from the request body
    html = request.json.get('html', '')

    # Convert HTML to Markdown
    try:
        markdown = html2text.html2text(html)
        return jsonify({"markdown": markdown}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

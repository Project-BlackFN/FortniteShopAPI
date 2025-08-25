import os
from flask import Flask
from .routes import shop_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(shop_bp)
    return app

if __name__ == '__main__':
    app = create_app()

    ROOT = os.path.dirname(os.path.dirname(__file__))
    ssl_cert_folder = os.path.join(ROOT, 'ssl')
    
    cert_file = os.path.join(ssl_cert_folder, "fullchain.pem")
    key_file = os.path.join(ssl_cert_folder, "privkey.pem")

    if os.path.exists(cert_file) and os.path.exists(key_file):
        app.run(host='0.0.0.0', port=443, ssl_context=(cert_file, key_file))
    else:
        app.run(host='0.0.0.0', port=80)

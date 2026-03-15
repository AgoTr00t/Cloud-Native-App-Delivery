from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

# Données simulées pour l'inventaire
inventory = [
    {"id": 1, "name": "Laptop Dell XPS", "quantity": 50, "price": 1299.99},
    {"id": 2, "name": "Souris Logitech", "quantity": 200, "price": 29.99},
    {"id": 3, "name": "Clavier Mécanique", "quantity": 150, "price": 89.99},
    {"id": 4, "name": "Écran 27 pouces", "quantity": 30, "price": 299.99},
    {"id": 5, "name": "Disque SSD 1To", "quantity": 75, "price": 149.99}
]

@app.route('/')
def home():
    hostname = socket.gethostname()
    
    # Construction du tableau HTML ligne par ligne
    table_rows = ""
    for item in inventory:
        table_rows += f"""
                <tr>
                    <td>{item['id']}</td>
                    <td><strong>{item['name']}</strong></td>
                    <td>{item['quantity']}</td>
                    <td>{item['price']:.2f} €</td>
                    <td>{'<span class="badge">En stock</span>' if item['quantity'] > 0 else 'Rupture'}</td>
                </tr>"""
    
    return f"""
    <html>
    <head>
        <title>Inventory Management App - TechLogix</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; }}
            .container {{ max-width: 1000px; margin: 0 auto; background: white; border-radius: 10px; padding: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); }}
            h1 {{ color: #333; text-align: center; border-bottom: 2px solid #667eea; padding-bottom: 10px; }}
            h2 {{ color: #667eea; }}
            table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
            th {{ background: #667eea; color: white; padding: 12px; text-align: left; }}
            td {{ padding: 10px; border-bottom: 1px solid #ddd; }}
            tr:hover {{ background-color: #f5f5f5; }}
            .badge {{ background: #28a745; color: white; padding: 5px 10px; border-radius: 20px; display: inline-block; }}
            .info {{ background: #e7f3ff; padding: 10px; border-radius: 5px; margin: 10px 0; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📦 Gestion de Stock - TechLogix</h1>
            <div class="info">
                <strong>Pod:</strong> {hostname} | <strong>Version:</strong> 1.0.0
            </div>
            
            <h2>Inventaire actuel</h2>
            <table>
                <tr>
                    <th>ID</th>
                    <th>Produit</th>
                    <th>Quantité</th>
                    <th>Prix (€)</th>
                    <th>Statut</th>
                </tr>
                {table_rows}
            </table>
            
            <h2>API Endpoints</h2>
            <ul>
                <li><code>GET /</code> - Page d'accueil</li>
                <li><code>GET /api/inventory</code> - Liste des produits (JSON)</li>
                <li><code>GET /health</code> - Health check</li>
            </ul>
            
            <p style="text-align: center; margin-top: 20px; color: #666;">
                Déployé avec ❤️ via Cloud-Native App Delivery
            </p>
        </div>
    </body>
    </html>
    """

@app.route('/api/inventory')
def get_inventory():
    return jsonify(inventory)

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "pod": socket.gethostname()})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
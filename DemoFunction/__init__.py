import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get('name', 'Team')

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Azure Function Demo</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #0078D4, #00BCF2);
                color: white;
                text-align: center;
                padding-top: 80px;
            }}
            .card {{
                background: white;
                color: #333;
                width: 60%;
                margin: auto;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            }}
            h1 {{
                color: #0078D4;
            }}
            footer {{
                margin-top: 30px;
                font-size: 14px;
                opacity: 0.8;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 Azure Function Live Demo</h1>
            <p>Hello <b>{name}</b>!</p>
            <p>This page is served directly from an Azure Function.</p>
            <p><b>Status:</b> Deployment successful ✅</p>
            <footer>
                Powered by Azure Functions (Python)
            </footer>
        </div>
    </body>
    </html>
    """

    return func.HttpResponse(html, mimetype="text/html")

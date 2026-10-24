from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AWS CI/CD Project</title>
        <style>
            :root {
                --bg-color: #f9e000;
                --card-bg: #1e3b2b;
                --text-main: red;
                --text-muted: #94a3b8;
                --accent: #38bdf8;
                --border: #334155;
            }
            * {
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }
            body {
                background-color: var(--bg-color);
                color: var(--text-main);
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                display: flex;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
                padding: 20px;
            }
            .card {
                background-color: var(--card-bg);
                border: 1px solid var(--border);
                border-radius: 12px;
                padding: 32px;
                width: 100%;
                max-width: 750px;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1);
            }
            h1 {
                font-size: 1.75rem;
                font-weight: 700;
                margin-bottom: 20px;
                color: var(--text-main);
                border-bottom: 2px solid var(--border);
                padding-bottom: 12px;
                text-align: center;
            }
            p {
                font-size: 0.95rem;
                line-height: 1.5;
                color: var(--text-muted);
                margin-bottom: 12px;
                display: flex;
                align-items: center;
            }
            p::before {
                content: "→";
                color: var(--accent);
                margin-right: 8px;
                font-weight: bold;
            }
            p:last-child {
                margin-bottom: 0;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Hello, World!</h1>
            <p>Welcome to my AWS CI/CD project.</p>
            <p>Containerized using Docker.</p>
            <p>Deploying using code build and code deploy</p>
            <p>i am new vanil</p>
            <p>Deployed using aws code build, code pipeline, code deploy.    </p>
            <p>After a huge struggle deployment and complete CICD project don it also had very less things to learn we will learn more inshallah</p>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

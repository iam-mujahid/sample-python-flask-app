from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <html data-bs-theme="dark">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AWS CI/CD Pipeline Dashboard</title>
        <!-- Bootstrap 5 CSS CDN -->
        <link href="https://jsdelivr.net" rel="stylesheet">
        <!-- Bootstrap Icons CDN -->
        <link href="https://jsdelivr.net" rel="stylesheet">
        <style>
            body {
                background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
                min-height: 100vh;
                font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            }
            .glass-card {
                background: rgba(30, 41, 59, 0.7);
                backdrop-filter: blur(12px);
                border: 1px solid rgba(255, 255, 255, 0.08);
                border-radius: 16px;
                box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
                transition: transform 0.2s ease, box-shadow 0.2s ease;
            }
            .glass-card:hover {
                transform: translateY(-2px);
                box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.5);
                border-color: rgba(99, 102, 241, 0.4);
            }
            .status-badge {
                font-size: 0.75rem;
                letter-spacing: 0.05em;
                padding: 0.5em 1em;
                border-radius: 20px;
            }
        </style>
    </head>
    <body class="d-flex align-items-center py-5">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-12 col-md-8 col-lg-6">
                    
                    <!-- Main Dashboard Card -->
                    <div class="glass-card p-4 p-sm-5 text-center text-white">
                        
                        <!-- Header Icon -->
                        <div class="mb-4">
                            <div class="d-inline-flex align-items-center justify-content-center bg-indigo-subtle rounded-circle p-3 bg-opacity-10" style="background: rgba(99, 102, 241, 0.15);">
                                <i class="bi bi-cloud-check text-indigo fs-1" style="color: #818cf8;"></i>
                            </div>
                        </div>

                        <!-- Title -->
                        <h1 class="h2 fw-bold mb-2 text-gradient" style="background: linear-gradient(to right, #fff, #cbd5e1); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                            Hello, World!
                        </h1>
                        <p class="text-secondary mb-4">Pipeline Status Room</p>

                        <hr class="border-secondary opacity-25 my-4">

                        <!-- Deployment Details List -->
                        <div class="text-start space-y-3">
                            
                            <div class="d-flex align-items-center justify-content-between p-3 rounded-3 mb-3" style="background: rgba(255,255,255,0.02);">
                                <div class="d-flex align-items-center gap-3">
                                    <i class="bi bi-git text-warning fs-4"></i>
                                    <div>
                                        <div class="fw-medium text-light">Project Scope</div>
                                        <div class="small text-muted">AWS CI/CD Pipeline</div>
                                    </div>
                                </div>
                                <span class="badge bg-success-subtle text-success status-badge">ACTIVE</span>
                            </div>

                            <div class="d-flex align-items-center justify-content-between p-3 rounded-3 mb-3" style="background: rgba(255,255,255,0.02);">
                                <div class="d-flex align-items-center gap-3">
                                    <i class="bi bi-box-seam text-info fs-4"></i>
                                    <div>
                                        <div class="fw-medium text-light">Environment</div>
                                        <div class="small text-muted">Containerized via Docker</div>
                                    </div>
                                </div>
                                <span class="badge bg-info-subtle text-info status-badge">READY</span>
                            </div>

                            <div class="d-flex align-items-center justify-content-between p-3 rounded-3" style="background: rgba(255,255,255,0.02);">
                                <div class="d-flex align-items-center gap-3">
                                    <i class="bi bi-display text-primary fs-4"></i>
                                    <div>
                                        <div class="fw-medium text-light">Deployment Target</div>
                                        <div class="small text-muted">Docker Desktop Localhost</div>
                                    </div>
                                </div>
                                <span class="badge bg-primary-subtle text-primary status-badge">RUNNING</span>
                            </div>

                        </div>

                        <!-- Footer Branding -->
                        <div class="mt-5 small text-muted">
                            <i class="bi bi-shield-lock-fill me-1"></i> Secured Local Development Node
                        </div>

                    </div>
                    
                </div>
            </div>
        </div>

        <!-- Bootstrap Bundle with Popper -->
        <script src="https://jsdelivr.net"></script>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

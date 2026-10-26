import os
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

PAGE = """
<!doctype html>
<html>
<head>
  <title>Student DevOps App</title>
  <style>
    body { font-family: Arial, sans-serif; background: #eef2f7; margin: 0; }
    nav { background: #1e3a5f; color: #fff; padding: 16px 24px;
          font-size: 20px; font-weight: bold; }
    .card { max-width: 640px; margin: 32px auto; background: #fff;
            padding: 32px; border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,.1); text-align: center; }
    h1 { color: #12284a; }
    table { width: 100%; margin-top: 24px; text-align: left;
            border-collapse: collapse; }
    td { padding: 8px; border-bottom: 1px solid #ddd; }
    .ok { color: #0a9d2f; font-weight: bold; }
  </style>
</head>
<body>
  <nav>Student DevOps App</nav>
  <div class="card">
    <h1>Deployed using a CI/CD Pipeline</h1>
    <p>Jenkins &rarr; Docker &rarr; Kubernetes (Minikube)</p>
    <table>
      <tr><td>Version (build)</td><td>{{ version }}</td></tr>
      <tr><td>Pod name</td><td>{{ pod }}</td></tr>
      <tr><td>Node</td><td>{{ node }}</td></tr>
      <tr><td>Status</td><td class="ok">Running</td></tr>
    </table>
  </div>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(
        PAGE,
        version=os.getenv("APP_VERSION", "dev"),
        pod=os.getenv("POD_NAME", "local"),
        node=os.getenv("NODE_NAME", "local"),
    )


@app.route("/health")
def health():
    return jsonify(status="healthy")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

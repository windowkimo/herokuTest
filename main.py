
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Heroku_Flask'

# ポート番号の設定
if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

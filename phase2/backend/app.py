from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("POSTGRES_DB", "app_db")
DB_USER = os.getenv("POSTGRES_USER", "user")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "password")

@app.route("/")
def home():
    return "Hello from Flask backend!"

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/db")
def db_check():
    try:
        conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS)
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        cur.fetchone()
        cur.close()
        conn.close()
        return jsonify(db="ok")
    except Exception as e:
        return jsonify(db="error", error=str(e)), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

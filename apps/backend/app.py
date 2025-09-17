import os
from flask import Flask, jsonify
from sqlalchemy import text, create_engine

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://siacard:siacard_pw@db:5432/siacard")
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

@app.get("/api/health")
def health():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        db_ok = True
    except Exception as e:
        db_ok = False
    return jsonify(ok=True, service="backend", db=db_ok)

# später: Auth + CRUD für Kategorien/Drinks (Preis, Bild, etc.)

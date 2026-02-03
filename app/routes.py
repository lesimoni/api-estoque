from fastapi import APIRouter
from .database import get_connection

router = APIRouter()

@router.get("/estoque")
def listar_estoque():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            nome_item,
            grupo,
            valor_item,
            quantidade_fisica
        FROM itens_estoque
    """)

    dados = [
        {
            "nome_item": r[0],
            "grupo": r[1],
            "valor_item": float(r[2] or 0),
            "quantidade_fisica": int(r[3] or 0)
        }
        for r in cur.fetchall()
    ]

    conn.close()
    return dados

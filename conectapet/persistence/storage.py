def salvar_linha(caminho, linha):
    with open(caminho, "a", encoding="utf-8") as f:
        f.write(linha.strip() + "\n")

def ler_linhas(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            return [l.strip() for l in f if l.strip()]
    except FileNotFoundError:
        return []
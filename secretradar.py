import os
import re
import sys

PADROES = [
    r"(?i)api[_-]?key\s*=\s*.+",
    r"(?i)token\s*=\s*.+",
    r"(?i)password\s*=\s*.+",
    r"(?i)senha\s*=\s*.+",
    r"(?i)secret\s*=\s*.+",
    r"-----BEGIN .*PRIVATE KEY-----",
]

PASTAS_IGNORADAS = [".git", "venv", ".venv", "__pycache__"]

ARQUIVOS_IGNORADOS = ["README.md", "secretradar.py"]

# A ferramenta ainda é inicial e pode gerar falsos positivos, 
# Por isso foram adicionadas regras simples para ignorar arquivos como README.md e o próprio script da ferramenta.

def mascarar(valor):
    if len(valor) <= 8:
        return "*" * len(valor)

    return valor[:4] + "*" * (len(valor) - 8) + valor[-4:]


def deve_ignorar_pasta(caminho):
    return any(pasta in caminho for pasta in PASTAS_IGNORADAS)


def deve_ignorar_arquivo(nome_arquivo):
    return nome_arquivo in ARQUIVOS_IGNORADOS


def analisar_pasta(pasta):
    encontrados = []

    for raiz, diretorios, arquivos in os.walk(pasta):
        if deve_ignorar_pasta(raiz):
            continue

        for arquivo in arquivos:
            if deve_ignorar_arquivo(arquivo):
                continue

            caminho_arquivo = os.path.join(raiz, arquivo)

            try:
                with open(caminho_arquivo, "r", encoding="utf-8", errors="ignore") as f:
                    linhas = f.readlines()
            except Exception:
                continue

            for numero_linha, linha in enumerate(linhas, start=1):
                for padrao in PADROES:
                    if re.search(padrao, linha):
                        encontrados.append({
                            "arquivo": caminho_arquivo,
                            "linha": numero_linha,
                            "conteudo": mascarar(linha.strip())
                        })

    return encontrados


def main():
    if len(sys.argv) < 2:
        print("Uso: python secretradar.py caminho/da/pasta")
        return

    pasta = sys.argv[1]
    encontrados = analisar_pasta(pasta)

    if not encontrados:
        print("Nenhuma possível credencial encontrada.")
        return

    print("\nPossíveis credenciais encontradas:\n")

    for item in encontrados:
        print(f"Arquivo: {item['arquivo']}")
        print(f"Linha: {item['linha']}")
        print(f"Conteúdo mascarado: {item['conteudo']}")
        print("-" * 40)

    print(f"\nTotal de achados: {len(encontrados)}")
    print("Aviso: os resultados podem conter falsos positivos.")


if __name__ == "__main__":
    main()
import os
import shutil
import datetime

def listar_pastas(diretorio):
    """Retorna uma lista de pastas dentro do diretório especificado."""
    return [nome for nome in os.listdir(diretorio) if os.path.isdir(os.path.join(diretorio, nome))]

def main():
    diretorio_origem = r"ORIGIN PATH (REPLACE THIS)"
    diretorio_backup = r"DESTINY PATH (REPLACE THIS)"

    # Listar pastas no diretório de origem
    pastas = listar_pastas(diretorio_origem)
    if not pastas:
        print("Nenhuma pasta encontrada em", diretorio_origem)
        return

    print("Pastas disponíveis:")
    for indice, pasta in enumerate(pastas, start=1):
        print(f"{indice}. {pasta}")

    try:
        escolha = int(input("Digite o número da pasta que deseja fazer backup: "))
    except ValueError:
        print("Por favor, digite um número válido!")
        return

    if escolha < 1 or escolha > len(pastas):
        print("Número inválido! Tente novamente.")
        return

    pasta_selecionada = pastas[escolha - 1]
    caminho_origem = os.path.join(diretorio_origem, pasta_selecionada)

    # Cria a string com data e hora no formato [yyyyMMdd_HHmm]
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    nome_backup = f"{pasta_selecionada}_{timestamp}"
    caminho_backup = os.path.join(diretorio_backup, nome_backup)

    try:
        shutil.copytree(caminho_origem, caminho_backup)
        print(f"Backup concluído com sucesso em: {caminho_backup}")
    except Exception as e:
        print("Erro ao realizar o backup:", e)

if __name__ == "__main__":
    main()

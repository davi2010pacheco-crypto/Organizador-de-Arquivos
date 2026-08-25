import os
import shutil

pasta = '/home/davi/Downloads'

grupos = {
    'Imagens': ['.jpg', '.jpeg', '.png'],
    'Documents': ['.odt', '.pdf', '.docx'],
    'Vídeos': ['.mp4'],
    'Músicas': ['.mp3'],
    'Compactados': ['.zip'],
    'Instaladores': ['.deb', '.rpm', '.run'],
}
categorias = {ext: pasta_dest for pasta_dest, exts in grupos.items() for ext in exts}

arquivos = os.listdir(pasta)

for arquivo in arquivos:
    caminho_completo = os.path.join(pasta, arquivo)

    if os.path.isdir(caminho_completo):
        continue

    _, extensao = os.path.splitext(arquivo)
    categoria = categorias.get(extensao.lower(), 'outros')

    pasta_destino = os.path.join(pasta, categoria)
    os.makedirs(pasta_destino, exist_ok=True)

    caminho_destino = os.path.join(pasta_destino, arquivo)
    shutil.move(caminho_completo, caminho_destino)







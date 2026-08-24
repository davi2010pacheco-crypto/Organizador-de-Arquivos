import os
import shutil

pasta = '/home/davi/Downloads'

arquivos = os.listdir(pasta)

categorias = {
	'.jpg': 'Imagens',
	'.jpeg': 'Imagens',
	'.odt': 'Documents',
	'.png': 'Imagens',
	'.pdf': 'Documents',
	'.docx': 'Documents',
	'.mp4': 'Vídeos',
	'.mp3': 'Músicas',
	'.zip': 'Compactados',
	'.deb': 'Instaladores',
	'.rpm': 'Instaladores',
	'.run': 'Instaladores'
}

for arquivo in arquivos:
	caminho_completo = os.path.join(pasta, arquivo)

	if os.path.isdir(caminho_completo):
		continue

	nome, extensao = os.path.splitext(arquivo)
	categoria = categorias.get(extensao, 'outros')
	pasta_destino = os.path.join(pasta, categoria)
	os.makedirs(pasta_destino, exist_ok=True)
	caminho_origem = os.path.join(pasta, arquivo)
	caminho_destino = os.path.join(pasta_destino, arquivo)
	shutil.move(caminho_origem, caminho_destino)







# Organizador de Arquivos Automático

Script em Python que organiza automaticamente os arquivos de uma pasta (ex: Downloads), movendo cada um para uma subpasta de acordo com sua extensão.

> **Feito para terminal Linux.** O script usa caminhos e comandos no padrão Linux (ex: `/home/usuario/Downloads`) e a automação (seção mais abaixo) é feita com `cron`, ferramenta nativa do Linux. Mas pode ser usador em Windows e MacOS.

## Como funciona

O script:

1. Lista todos os arquivos dentro da pasta escolhida
2. Ignora subpastas (para não tentar mover pastas para dentro de si mesmas)
3. Identifica a extensão de cada arquivo
4. Consulta um dicionário que mapeia extensão
5. Cria a pasta de destino, caso ainda não exista
6. Move o arquivo para a pasta correta

Arquivos com extensões não cadastradas vão para uma pasta chamada `outros`.

## Categorias organizadas

| Extensão | Pasta destino |
|---|---|
| `.jpg`, `.jpeg`, `.png` | Imagens |
| `.pdf`, `.docx`, `.odt` | Documents |
| `.mp4` | Vídeos |
| `.mp3` | Músicas |
| `.zip` | Compactados |
| `.deb`, `.rpm`, `.run` | Instaladores |
| outras | outros |

## Módulos usados

- `os` — listar arquivos, verificar se é pasta (`os.path.isdir`), separar extensão (`os.path.splitext`), montar caminhos (`os.path.join`) e criar pastas (`os.makedirs`)
- `shutil` — mover arquivos (`shutil.move`)

## Como usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/organizador-de-arquivos.git
   cd organizador-de-arquivos
   ```

2. Abra o arquivo `codigo.py` e edite a variável `pasta` para o caminho que você quer organizar:
   ```python
   pasta = "/home/seu_usuario/Downloads"
   ```

3. Edite o dicionário `categorias` para adicionar ou mudar extensões e pastas de destino.

4. Rode o script pelo terminal Linux:
   ```bash
   python3 codigo.py
   ```

## Automação (opcional)

É possível agendar a execução automática do script usando o `cron`, o agendador de tarefas nativo do Linux. Para rodar todo dia num horário em que desejar, por exemplo, abra o terminal e edite o crontab com `crontab -e`, depois adicione esta linha:

```
0 00 * * * /usr/bin/python3 /caminho/completo/para/codigo.py
```



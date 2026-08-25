# Organizador de Arquivos Automático

Script em Python que organiza automaticamente os arquivos de uma pasta, movendo cada um para uma subpasta de acordo com sua extensão.

> **Feito para terminal Linux.** O script usa caminhos e comandos no padrão Linux (ex: `/home/usuario/Downloads`) e a automação (seção mais abaixo) é feita com `cron`, ferramenta nativa do Linux. Mas pode ser usador em Windows e MacOS.

O script:

1. Lista todos os arquivos dentro da pasta escolhida
2. Ignora subpastas (para não tentar mover pastas para dentro de si mesmas)
3. Identifica a extensão de cada arquivo
4. Consulta um dicionário que mapeia extensão
5. Cria a pasta de destino, caso ainda não exista
6. Move o arquivo para a pasta correta

Arquivos com extensões não cadastradas vão para uma pasta chamada `outros`.






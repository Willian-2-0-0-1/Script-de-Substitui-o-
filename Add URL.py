import re

# Abrir o arquivo HTML
with open(r'C:\Users\WILL\Downloads\index.html', 'r') as file:
    html = file.read()

# Encontrar todas as ocorrências de "/assets/" usando expressão regular
matches = re.findall(r'/assets/', html)

# Criar uma lista para armazenar as URLs já atualizadas
updated_urls = []

# Adicionar a URL completa antes de cada ocorrência, se ainda não foi atualizada
for match in matches:
    updated_url = 'https://uniipar.com/br' + match
    if updated_url not in updated_urls:
        html = html.replace(match, updated_url)
        updated_urls.append(updated_url)

# Salvar o arquivo HTML com as URLs atualizadas
with open(r'C:\Users\WILL\Downloads\output.html', 'w') as file:
    file.write(html)

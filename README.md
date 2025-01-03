# Sacada Web - Blog Pessoal

## Descrição
Este projeto é um blog pessoal desenvolvido com Django, permitindo que usuários criem, editem e visualizem postagens organizadas por categorias e datas. Além disso, o projeto possui um dashboard administrativo para gerenciar as postagens e categorias de forma eficiente.

## Funcionalidades
- **Postagens**: Criação, edição e listagem de artigos com título, descrição, imagem e data de publicação.
- **Dashboard**: Interface administrativa para gerenciar postagens e categorias.
- **Busca**: Campo de busca para localizar postagens específicas.
- **Categorias**: Navegação por categorias temáticas.
- **Últimos Artigos**: Listagem dos artigos mais recentes na barra lateral.
- **Upload de Imagens**: Suporte para adicionar imagens às postagens.

## Tecnologias Utilizadas
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Banco de Dados**: SQLite (padrão do Django, configurável para outros SGBDs)

## Estrutura do Projeto
```plaintext
sacadaweb/
├── core/               # Configuração principal do projeto
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── env/                # Ambiente virtual (não deve ser versionado)
├── media/              # Diretório para arquivos enviados (upload de imagens)
├── posts_app/          # App responsável pelas postagens do blog
│   ├── migrations/     # Arquivos de migração do banco de dados
│   ├── templates/      # Templates HTML relacionados às postagens
│   ├── static/         # Arquivos estáticos do app
│   ├── admin.py        # Configuração do dashboard administrativo
│   ├── apps.py         # Configurações do app
│   ├── models.py       # Modelos do banco de dados
│   ├── views.py        # Lógica de visualização das páginas
│   └── ...
├── static/             # Arquivos estáticos globais (CSS, JS, imagens)
├── templates/          # Templates HTML globais
├── db.sqlite3          # Banco de dados SQLite
├── .gitignore          # Arquivos/diretórios ignorados pelo Git
├── manage.py           # Gerenciador do Django
└── README.md           # Documentação do projeto

## Passo a Passo
Clone o repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/sacada-web.git
cd sacada-web
Crie um ambiente virtual e ative-o:

bash
Copiar código
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate     # Para Windows
Instale as dependências:



Frontend: http://127.0.0.1:8000/
![image](https://github.com/user-attachments/assets/2b635e0c-c006-4a8d-91c5-d350ed5c1f23)


Dashboard: http://127.0.0.1:8000/admin/
![image](https://github.com/user-attachments/assets/a7dccb0b-3cc3-4c7d-b2fb-ae13fb8cb48b)


## Melhorias Futuras
Sistema de comentários para os posts.
Integração com redes sociais.
Implementação de filtros avançados na busca.
Contribuição
Contribuições são bem-vindas! Para contribuir:

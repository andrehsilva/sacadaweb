Sacada Web - Blog Pessoal
Descrição
Este é um projeto de blog pessoal desenvolvido com o framework Django. Ele permite criar, editar e visualizar postagens organizadas por categorias e datas. O site apresenta uma interface amigável para leitura e navegação.

Funcionalidades
Postagens: Criação, edição e listagem de artigos do blog com título, descrição, imagem e data de publicação.
Busca: Campo de busca para encontrar postagens específicas.
Categorias: Navegação por categorias temáticas.
Últimos Artigos: Listagem dos artigos mais recentes na barra lateral.
Tecnologias Utilizadas
Backend: Django (Python)
Frontend: HTML, CSS, Bootstrap
Banco de Dados: SQLite (padrão do Django, pode ser configurado para outros SGBDs)
Como Executar o Projeto
Pré-requisitos
Python 3.8 ou superior
Pip (gerenciador de pacotes do Python)
Virtualenv (opcional, mas recomendado)

Passo a Passo
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



Melhorias Futuras
Sistema de comentários para os posts.
Integração com redes sociais.
Filtros avançados para busca.
Contribuição
Contribuições são bem-vindas! Para contribuir:

Faça um fork do projeto.
Crie uma branch para sua feature (git checkout -b minha-feature).
Faça o commit das mudanças (git commit -m 'Adiciona nova feature').
Envie para o branch principal (git push origin minha-feature).
Abra um Pull Request.
Se precisar de ajustes ou detalhes adicionais, é só avisar! 😊



Estrutura Atualizada do Projeto
plaintext
Copiar código
sacadaweb/
├── core/               # Contém a configuração principal do projeto
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── env/                # Ambiente virtual (não deve ser versionado no Git)
├── media/              # Diretório para arquivos enviados (upload de imagens, etc.)
├── posts_app/          # App responsável pelas postagens do blog
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── ...
├── static/             # Arquivos estáticos (CSS, JS, imagens)
├── templates/          # Templates HTML do projeto
├── db.sqlite3          # Banco de dados SQLite
├── .gitignore.txt      # Arquivos e diretórios ignorados pelo Git
├── manage.py           # Gerenciador do Django
└── README.md           # Documentação do projeto

Explicação das Pastas e Arquivos
core/: Diretório principal com a configuração global do projeto Django.
env/: Diretório do ambiente virtual. Não deve ser versionado no controle de versão.
media/: Armazena os arquivos de upload, como imagens associadas às postagens.
posts_app/: App específico para gerenciar postagens, contendo:
migrations/: Migrações do banco de dados para o app.
templates/: Templates HTML relacionados às postagens.
static/: Arquivos estáticos do app, como estilos e scripts.
models.py: Modelos para o banco de dados.
views.py: Lógica de visualização das páginas.
static/: Diretório global para arquivos estáticos.
templates/: Diretório global para templates HTML.
db.sqlite3: Banco de dados padrão do Django.
manage.py: Script de gerenciamento do Django.
README.md: Arquivo de documentação do projeto.

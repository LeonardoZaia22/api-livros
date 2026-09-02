# API de Livros - Sistemas Web II

Este é o meu projeto desenvolvido para a disciplina de Sistemas Web II (SW-II), onde construo uma aplicação web completa para gerenciamento de livros. O projeto representa minha jornada de aprendizado desde o banco de dados até uma interface visual funcional.

## Sobre o Projeto

Este projeto é a minha atividade avaliativa do 3º Bimestre, onde aplico na prática todos os conceitos aprendidos em aula. Desenvolvi uma API RESTful utilizando FastAPI e MySQL, e construí uma interface web para interagir com o sistema de forma intuitiva.

### O que minha aplicação faz?

Minha aplicação permite gerenciar um acervo de livros com as seguintes informações:
- ID único para identificação
- Título do livro
- Autor
- Ano de publicação
- Status de disponibilidade

## Minha Jornada de Desenvolvimento

### Etapa 1: Fundação do Projeto
Comecei configurando todo o ambiente de desenvolvimento: instalei as dependências necessárias, criei o banco de dados `biblioteca_db` no MySQL via XAMPP e estabeleci a conexão entre Python e o banco. A primeira rota que criei foi a de saúde, para verificar se tudo estava funcionando.

### Etapa 2: Construindo o Coração da API
Nesta fase, criei o modelo `Livro` com SQLAlchemy, desenvolvi os schemas para validação de dados e implementei as primeiras rotas: POST para cadastrar livros e GET para listar e consultar o acervo.

### Etapa 3: CRUD Completo
Finalizei as operações fundamentais da API implementando as rotas PUT para atualização e DELETE para exclusão de livros. Também adicionei tratamento de erros para garantir que a API seja robusta e confiável.

### Etapa 4: Interface Visual
A última etapa foi a mais emocionante: transformei minha API em uma aplicação web completa com HTML, CSS e JavaScript. Agora é possível cadastrar, listar, editar e excluir livros diretamente pelo navegador.

## Tecnologias que Utilizei

- **Backend**: Python com FastAPI
- **Servidor**: Uvicorn
- **Banco de Dados**: MySQL gerenciado pelo phpMyAdmin no XAMPP
- **ORM**: SQLAlchemy com PyMySQL
- **Frontend**: HTML, CSS e JavaScript
- **Ferramentas**: VS Code e GitHub

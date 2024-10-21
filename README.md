
# Sistema de Gestão de Tickets

Este é um projeto básico de gerenciamento de tickets utilizando **Flask** e **SQLite**.

## Configuração do Ambiente

Para configurar o ambiente, siga os seguintes passos, garantindo que todos os arquivos estejam na mesma pasta:

1. Inicialize o banco de dados SQLite com o script SQL fornecido:
   ```bash
   sqlite3 data.db < script.sql
   ```

2. Instale as dependências do projeto:
   ```bash
   pip install Flask
   ```

## Sumário dos Endpoints

### Tickets

- **GET /tickets**  
  Obter todos os tickets.

- **POST /tickets**  
  Criar um novo ticket.

- **PUT /tickets/<int:ticket_id>**  
  Atualizar um ticket existente.

- **GET /tickets/abertos**  
  Obter todos os tickets com status "aberto" (Status = 0).

- **GET /tickets/andamento**  
  Obter todos os tickets com status "em andamento" (Status = 1).

- **GET /tickets/completos**  
  Obter todos os tickets com status "completo" (Status = 2).

- **GET /tickets/usuario/<int:usuario_id>**  
  Obter todos os tickets atribuídos a um usuário específico.

### Usuários

- **GET /usuarios**  
  Obter todos os usuários.

- **POST /usuarios**  
  Criar um novo usuário.

- **GET /usuarios/<int:usuario_id>**  
  Obter um usuário pelo ID.

- **GET /usuarios/login/<string:login>**  
  Obter um usuário pelo login.

## Exemplos de Requisição

### GET /tickets

Resposta:
```json
[
    {
        "Descricao": "Descrição do problema...",
        "ID": 1,
        "ID_pessoa": null,
        "Prioridade": 1,
        "Status": 0,
        "Titulo": "Problema no sistema"
    },
    {
        "Descricao": "Descrição do erro...",
        "ID": 2,
        "ID_pessoa": null,
        "Prioridade": 3,
        "Status": 0,
        "Titulo": "Erro de carregamento"
    }
]
```

### POST /tickets

Requisição:
```json
{
    "Titulo": "Título do Ticket",
    "Descricao": "Descrição detalhada do problema",
    "Prioridade": 1
}
```

### PUT /tickets/<int:ticket_id>

Requisição:
```json
{
    "Prioridade": 3,
    "Status": 1,
    "ID_pessoa": 5
}
```

### POST /usuarios

Requisição:
```json
{
    "Login": "novo_usuario",
    "Senha": "nova_senha"
}
```

## Tecnologias Utilizadas

- **Flask** - Framework web.
- **SQLite** - Banco de dados utilizado para armazenar os tickets e usuários.

## Como Executar

1. Configure o banco de dados e as dependências conforme descrito acima.
2. Inicie o servidor Flask:
   ```bash
   flask run
   ```
3. Acesse a API utilizando as rotas descritas na seção de endpoints.

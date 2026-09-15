# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Você aprenderá a construir uma API REST com FastAPI, organizando rotas, recebendo dados JSON e retornando respostas com códigos HTTP apropriados. Ao final, sua API permitirá gerenciar atividades escolares em memória.

## 📝 Tasks

### 🛠️ Criar a API e uma rota de status

#### Descrição

Instale o FastAPI e o Uvicorn, execute o arquivo inicial e complete a rota de status da aplicação. Use a documentação interativa gerada automaticamente pelo FastAPI para testar a rota.

#### Requisitos

O programa concluído deve:

- Criar uma instância de `FastAPI` com um título descritivo
- Disponibilizar `GET /health` ou `GET /` indicando que a API está funcionando
- Iniciar com `uvicorn starter-code:app --reload`
- Permitir acessar a documentação interativa em `/docs`

### 🛠️ Implementar endpoints de atividades

#### Descrição

Crie endpoints para listar todas as atividades e adicionar uma nova atividade. Os dados podem ser armazenados em uma lista em memória, sem banco de dados.

#### Requisitos

O programa concluído deve:

- Disponibilizar `GET /activities` para retornar todas as atividades
- Disponibilizar `POST /activities` para criar uma atividade
- Aceitar no mínimo os campos `title`, `subject` e `completed`
- Retornar a atividade criada com um identificador único
- Retornar o status HTTP `201` ao criar uma atividade

Um exemplo de requisição para `POST /activities` é:

```json
{
  "title": "Read chapter 3",
  "subject": "Computer Science",
  "completed": false
}
```

### 🛠️ Adicionar validação e operações CRUD

#### Descrição

Evolua a API para validar os dados recebidos e permitir consultar, atualizar e remover uma atividade específica pelo seu identificador.

#### Requisitos

O programa concluído deve:

- Rejeitar títulos vazios e atividades sem uma disciplina válida usando modelos Pydantic
- Disponibilizar `GET /activities/{activity_id}` para consultar uma atividade
- Disponibilizar `PUT /activities/{activity_id}` para atualizar uma atividade
- Disponibilizar `DELETE /activities/{activity_id}` para remover uma atividade
- Retornar `404 Not Found` quando o identificador não existir
- Usar tipos e respostas coerentes para cada endpoint

Teste pelo menos estes casos na documentação `/docs`:

```text
GET /activities/1       -> 200 quando a atividade existe
GET /activities/999     -> 404 quando a atividade não existe
DELETE /activities/1    -> 200 ou 204 quando a remoção funciona
```

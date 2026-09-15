# 📘 Assignment: Testing FastAPI with pytest

## 🎯 Objective

Você aprenderá a escrever testes automatizados para uma API FastAPI usando `pytest` e `TestClient`. Ao final, sua suíte de testes verificará respostas bem-sucedidas, validação de dados e erros HTTP de uma API de atividades escolares.

## 📝 Tasks

### 🛠️ Configurar o ambiente de testes

#### Descrição

Instale as dependências necessárias e crie um arquivo chamado `test_api.py`. Use o `TestClient` do FastAPI para fazer requisições à aplicação sem iniciar um servidor separado.

#### Requisitos

O programa concluído deve:

- Instalar `fastapi`, `httpx` e `pytest`
- Importar `app` de `starter_code.py` e criar um cliente de testes
- Ter um teste para `GET /health`
- Verificar que a resposta tem status `200` e o JSON `{"status": "ok"}`
- Executar com o comando `pytest -q`

### 🛠️ Testar o fluxo de criação de atividades

#### Descrição

Escreva testes para o endpoint que cria atividades e para o endpoint que lista atividades. Cada teste deve verificar tanto o código HTTP quanto os dados importantes da resposta.

#### Requisitos

O programa concluído deve:

- Testar `POST /activities` com uma atividade válida
- Verificar o status `201 Created`
- Verificar que a resposta contém `title`, `subject`, `completed` e um `id` numérico
- Testar `GET /activities` e verificar que a atividade criada aparece na lista
- Enviar dados JSON usando o cliente de testes

Um exemplo de corpo válido é:

```json
{
  "title": "Review functions",
  "subject": "Computer Science",
  "completed": false
}
```

### 🛠️ Cobrir validação e erros da API

#### Descrição

Adicione testes para os casos em que o cliente envia dados inválidos ou procura uma atividade inexistente. Use nomes de teste descritivos para deixar claro qual comportamento está sendo protegido.

#### Requisitos

O programa concluído deve:

- Verificar que um título vazio retorna `422 Unprocessable Entity`
- Verificar que uma disciplina vazia retorna `422 Unprocessable Entity`
- Verificar que consultar uma atividade inexistente retorna `404 Not Found`
- Verificar que excluir uma atividade inexistente retorna `404 Not Found`
- Ter pelo menos seis testes independentes e todos devem passar com `pytest -q`
- Usar fixtures ou funções auxiliares quando isso evitar repetição significativa

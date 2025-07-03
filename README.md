# Simulador de Suporte Bancário

Projeto simples com:

- SQLite para dados de clientes
- API Flask para status de transações
- Python para consultar clientes ativos e mostrar status da última transação

## Como usar

1. Crie o banco: `sqlite3 support.db < database/bank_users.sql`
2. Rode a API: `python api/mock_bank_api.py`
3. Execute o script: `python support/check_accounts.py`

# SaveQue$t Backend

Backend da plataforma SaveQue$t, uma aplicação de construção de hábitos financeiros com gamificação.

## Arquitetura

- Monólito modular
- Vertical Slice
- DDD pragmático
- Clean Architecture
- CQRS leve

## Requisitos

- Python 3.14+
- PostgreSQL

## Ambiente local

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
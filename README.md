## Проект чата с локальной большой языковой моделью и биллинговой системой

### Запуск проверки LLM-сервиса
```bash
OPENAI_API_KEY=some uv run python -m src.apps.llm_test
```

### Запуск бэкенда
```bash
OPENAI_API_KEY=some uv run fastapi dev ./src/apps/backend.py
```

### Запуск фронтенда
```bash
uv run fastapi dev ./src/apps/frontend.py
```
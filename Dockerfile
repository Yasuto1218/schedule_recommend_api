FROM python:3.10-slim-buster

WORKDIR /usr/src

RUN pip install --upgrade pip \
    && pip install poetry \
    && pip install uvicorn \
    && rm -rf /root/.cache/pip
    

COPY pyproject.toml poetry.lock* ./

# 依存関係のインストール
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-dev

COPY src/ /usr/src/

# コンテナの8000ポートを外部に公開
EXPOSE 8000

# FastAPIサーバーをsrc/main.pyから起動
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
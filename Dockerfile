FROM python:3.7
WORKDIR /usr/src/app
RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY . .
RUN poetry install
CMD ["poetry", "run", "start"]
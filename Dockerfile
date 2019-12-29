FROM python:3.7
WORKDIR /usr/src/app
RUN pip install poetry
RUN poetry config settings.virtualenvs.create false
COPY . .
RUN poetry install
CMD ["poetry", "run", "start"]
FROM python:3.8
LABEL maintainer="antonklyukin@gmail.com"

COPY requirements.txt /opt/otus-lotto/requirements.txt

WORKDIR /opt/otus-lotto

RUN pip install -r requirements.txt

COPY . /opt/otus-lotto

CMD ["/bin/bash"]

# Пример запуска приложения внутри контейнера
# python -m otus-lotto
# pytest tests/test_card.py
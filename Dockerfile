FROM python:3.8

WORKDIR /app

RUN pip install django && pip install openai
RUN apt install -y git

CMD ["git pull"]
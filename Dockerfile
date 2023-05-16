FROM python:3.8

WORKDIR /app

RUN pip install django && pip install openai

ENV OPENAI_API_KEY=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

CMD ["python3", "mygpt/manage.py", "runserver", "0.0.0.0:80"]
FROM python:3.8

WORKDIR /app

RUN pip install django && pip install openai
RUN apt install -y git

CMD ["git pull"]
CMD ["python3", "mygpt/manage.py", "runserver", "0.0.0.0:80"]
FROM python:3.8.2-alpine3.11

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY renamer.py ./

CMD [ "python","-u" , "./renamer.py" ]
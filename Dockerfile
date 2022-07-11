FROM python:3.8-alpine

#Copy project
COPY . .

#set enviroment
ENV PYTHONPATH=${PYTHONPATH}:${PWD} 
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

#install dependencies
RUN apk add --update --virtual .tmp-build-deps \
    gcc libc-dev linux-headers  \
    && apk add libffi-dev


#configure poetry
RUN pip install --upgrade pip
RUN pip3 install poetry

RUN poetry build -f wheel
RUN pip install dist/*.whl

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

ENTRYPOINT ["./entrypoint.sh"]
ARG PYTHON_VERSION=python3.8

FROM tiangolo/uvicorn-gunicorn-fastapi:${PYTHON_VERSION}

COPY ./requirements.txt /usr/config/requirements.txt

WORKDIR /usr/app

RUN python3 -m pip install --upgrade pip \
    && pip install -r /usr/config/requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
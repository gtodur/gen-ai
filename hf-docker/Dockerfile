FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN useradd guru
USER guru

ENV HOME=/home/guru \
    PATH=/home/guru/.local/bin:$PATH
    
WORKDIR $HOME/app
COPY --chown=guru . $HOME/app

EXPOSE 7860:7860

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
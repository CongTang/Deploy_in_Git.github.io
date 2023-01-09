FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .

CMD ["panel", "serve", "/code/main.oy","--address", "0.0.0.0", "--port", "7860","--allow-websocket-origin","VictorTang-PanelTrial.hf.space"]

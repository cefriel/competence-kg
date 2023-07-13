FROM python:3.8

WORKDIR /code

RUN pip3 install --no-cache-dir --upgrade pip

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY script/ .
RUN mkdir data

COPY commands.sh /code/commands.sh
RUN ["chmod", "+x", "/code/commands.sh"]

ENTRYPOINT ["/code/commands.sh"]
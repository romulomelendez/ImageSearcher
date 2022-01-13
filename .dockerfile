FROM python:3

RUN mkdir -p /usr/src/app
COPY . /usr/src/app
RUN pip install
WORKDIR /usr/src/app
CMD ["flask", "run"]
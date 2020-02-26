FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /moviesite
WORKDIR /moviesite
COPY requirements.txt /moviesite/
RUN pip install -i https://pypi.douban.com/simple -r requirements.txt
COPY . /moviesite/
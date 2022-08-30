FROM python:3.8
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1
RUN mkdir /local
ADD . /local
RUN pip install --upgrade pip && \
    pip install -r /local/requirements.txt
EXPOSE 8888
CMD bash -c "gunicorn portfolio.wsgi --workers 3 --threads 100 --max-requests 1000 --max-requests-jitter 15 -b 0.0.0.0:8888"
WORKDIR /local

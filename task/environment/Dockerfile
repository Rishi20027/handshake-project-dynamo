FROM python:3.11-slim@sha256:83597c4860b093126f34346e45877c44e94200673f4e24eb37452d3a669ff6ef

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log

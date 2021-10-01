FROM python:3.8-buster
EXPOSE 8080
RUN mkdir -p /fastapi_python_template
COPY . /fastapi_python_template/
WORKDIR /fastapi_python_template
RUN pip install --use-feature=2020-resolver -r requirements.txt
CMD ["python", "run.py", "server"]
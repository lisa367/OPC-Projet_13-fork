FROM ubuntu
# FROM python:3.8.6-alpine
RUN apt-get update && \
apt-get install -y git && \
apt-get install -y python3.8.3 && \
apt-get install -y python3-pip
RUN apt-get python3.10-venv
# RUN apt-get install -y git
WORKDIR /OPC-Projet_13

COPY . $WORKDIR

# RUN git clone https://github.com/lisa367/OPC-Projet_13.git 
RUN python3 -m venv venv
RUN . venv/bin/activate
RUN pip install -r requirements.txt


# ENTRYPOINT ["gunicorn", "core.wsgi"]
CMD ["python", "manage.py", "runserver"]
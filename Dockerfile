FROM ubuntu
# FROM python:3.8.6-alpine
RUN apt-get update
RUN apt-get install -y python3.8.3
RUN apt-get install -y python3-pip
# RUN apt-get install -y git
WORKDIR /OPC-Projet_13

COPY . $WORKDIR

# RUN git clone 
# RUN pyton3 -m venv venv
# RUN source venv/bin/activate
# RUN source venv/bin/activate
RUN pip install -r requirements.txt


# ENTRYPOINT ["gunicorn", "core.wsgi"]
CMD ["python", "manage.py", "runserver"]
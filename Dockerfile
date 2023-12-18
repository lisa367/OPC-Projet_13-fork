FROM python:3.8.6-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
EXPOSE 8000

WORKDIR /OPC-Projet_13
COPY . $WORKDIR
RUN pip install -r requirements.txt

# ENTRYPOINT ["gunicorn", "core.wsgi"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# FROM ubuntu
# RUN apt-get update && \
    #apt-get install -y git && \
    #apt-get install -y python3 && \
    #apt-get install -y python3-pip
# RUN apt-get install -y python3.10-venv
# RUN git clone https://github.com/lisa367/OPC-Projet_13.git 


# WORKDIR /OPC-Projet_13
# COPY . $WORKDIR

# RUN python3 -m venv venv
# RUN . venv/bin/activate
# RUN pip install -r requirements.txt

# ENV PATH="$PATH:$WORKDIR/venv/bin/python"
# ENV PATH="${PATH}:$WORKDIR/venv/bin/python"

# ENTRYPOINT ["gunicorn", "core.wsgi"]
# CMD ["python", "manage.py", "runserver",]
# CMD ["ls", "-a"]
# CMD ["python", "--version"]
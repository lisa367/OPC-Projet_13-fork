FROM ubuntu
RUN apt-get install git

# WORKDIR /OPC-Projet_13

# RUN git clone 
RUN pyton3 -m venv venv
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
# RUN pytest
RUN python manage.py runserver

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
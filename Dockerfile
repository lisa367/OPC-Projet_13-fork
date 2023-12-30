FROM python:3.8.6-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /OPC-Projet_13
COPY . $WORKDIR
RUN pip install -r requirements.txt
RUN python manage.py collectstatic

ENTRYPOINT ["gunicorn", "oc_lettings_site.wsgi"]
# EXPOSE 8000
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM python:3.12-slim 
RUN groupadd -r groupflask && useradd -r -g groupflask userfdjango
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFEED0=1

RUN pip install --upgrade pip
RUN pip install flask psycopg2-binary
WORKDIR /app-example
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn
COPY . .
EXPOSE 8000

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "sitedjango.wsgi:application"]

USER userfdjango







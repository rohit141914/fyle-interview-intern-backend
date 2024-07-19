FROM python:3.8
WORKDIR .
COPY . .
RUN pip install virtualenv 
RUN pip install flask
RUN pip install -r requirements.txt
ENV FLASK_APP="core/server.py"
RUN rm core/store.sqlite3
EXPOSE 7755
RUN flask db upgrade -d core/migrations/
CMD ["pytest","--cov"]


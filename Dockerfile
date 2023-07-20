FROM python

RUN mkdir /app

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 3000

CMD ["flask","run","-h","0.0.0.0","-p","3000"]

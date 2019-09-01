FROM python:3.7.4
ENV PYTHONUNBUFFERED 1
RUN apt update
RUN apt install -y \
        g++ \
        gcc \
        unixodbc-dev        
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - 
RUN curl https://packages.microsoft.com/config/debian/8/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt update 
RUN ACCEPT_EULA=Y apt install -y msodbcsql17
RUN apt-get clean
RUN pip install pipenv
RUN mkdir /code
WORKDIR /code
ADD Pipfile Pipfile.lock /code/
RUN pipenv install --dev --system --verbose

ADD . /code/

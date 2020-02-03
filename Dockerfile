FROM python:3
ENV PYTHONUNBUFFERED 1

LABEL LAURENT Louis

RUN mkdir /code
WORKDIR /code

COPY pip_requirements.txt /code
RUN pip3 install --no-cache-dir -r pip_requirements.txt

ADD . /code

RUN rm api-python/settings.liv.py
RUN mv settings.py api-python/

EXPOSE 8000

RUN chmod 760 /code/starter.sh

ENTRYPOINT [ "/code/starter.sh" ]
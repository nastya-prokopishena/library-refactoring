FROM jenkins/jenkins:lts

USER root

# Встановлення Python та залежностей
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install pytest pymongo flask

# Встановлення Docker для використання всередині контейнера (опціонально)
RUN apt-get install -y docker.io

USER jenkins
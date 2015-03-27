FROM aexea/django-base-py2
MAINTAINER Arne Schauf

USER root
RUN pip install raven
WORKDIR hopperpw
ENTRYPOINT ["./start.sh"]
CMD ["web"]

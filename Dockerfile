FROM aexea/django-base-py2
MAINTAINER Arne Schauf

USER root
WORKDIR hopperpw
ENTRYPOINT ["./start.sh"]
CMD ["web"]

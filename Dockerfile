FROM aexea/django-base-py2
MAINTAINER Arne Schauf

WORKDIR hopperpw
ENTRYPOINT ["./start.sh"]
CMD ["web"]

FROM aexea/django-base
MAINTAINER Arne Schauf

WORKDIR hopperpw
ENTRYPOINT ["./start.sh"]
CMD ["web"]

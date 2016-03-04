FROM python:2-onbuild
ENV VOTER_LOOKUP_DATABASE /voter.db
CMD ["gunicorn", "webapp:application", "-b", "0.0.0.0:8080"]
EXPOSE 8080

MAINTAINER Anand Chitipothu <anandology@gmail.com>
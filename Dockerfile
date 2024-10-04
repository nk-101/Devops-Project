FROM python:3
# LABEL Maintainer=" "

# WORKDIR /usr/app/src
ADD task.py .

CMD ["python", "-u", "task.py"]
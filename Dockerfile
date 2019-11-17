FROM python:3

WORKDIR /script

#Get tools
RUN apt-get update && apt-get install -y --no-install-recommends gpsbabel && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Copy data and scripts
COPY export.zip .
COPY script.py .
COPY extractnconvertexport2gpx.sh .

CMD ./extractnconvertexport2gpx.sh && python ./script.py
#ENTRYPOINT ["tail", "-f", "/dev/null"]
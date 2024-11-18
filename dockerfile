# use an official Python runtime s a parent image
FROM python:3.9-slim

#working directory in the container
WORKDIR /app

#Copy the current directory contents into the conatainer at /app
COPY . /app

#Install any needed packeges specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install uvicorn separately and verify the installation
RUN pip install uvicorn && pip show uvicorn

#Make port 8000 available to the world outside thid  containert
EXPOSE 8000

#Define environment variable 
ENV PYTHONNUNBUFFERD=1

#Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

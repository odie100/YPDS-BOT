FROM python:3.10

# Set unbuffered output for python
ENV PYTHONUNBUFFERED 1

# Create app directory
WORKDIR /bot

# Install app dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Bundle app source
COPY . .

# Expose port
EXPOSE 8000

# Specify the command to run Django directly
CMD ["/bin/sh", "-c", "python main.py"]

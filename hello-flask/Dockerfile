
# FROM python:3.8-slim

# # Set working directory
# WORKDIR /app

# # Install required OS-level packages for mysqlclient
# RUN apt-get update && apt-get install -y \
#     gcc \
#     default-libmysqlclient-dev \
#     build-essential \
#     pkg-config \
#     && rm -rf /var/lib/apt/lists/*

# # Copy your project files
# COPY . .

# # Install Python dependencies
# RUN pip install flask mysqlclient

# # Expose Flask's port
# EXPOSE 5002

# # Start the app
# CMD ["python", "app.py"]



# Stage 1: Builder
FROM python:3.8-slim as build

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Stage 2: Runtime
FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    gcc \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY --from=build /app /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5002

CMD ["python", "app.py"]

# Docker Secret Support Layer for Docker Swarm

This project provides a **Docker image layer** that adds **Docker Swarm secret support** to Docker images that do not natively support it. It enables the conversion of environment variables with names ending in `_SECRET` into variables without the `_SECRET` suffix, and sets their values to the content of the corresponding mounted Docker Swarm secrets.

## Features

- Automatically detects environment variables ending with `_SECRET`.
- Converts these environment variables by removing the `_SECRET` suffix.
- Loads the value of the corresponding mounted secret and assigns it to the environment variable without the `_SECRET` suffix.
- Seamlessly integrates with Docker Swarm secrets management system.
- Ideal for applications and Docker images that do not natively support Docker Swarm secrets.

## How it Works

Docker Swarm secrets are securely mounted into containers, and you can specify secrets as environment variables. However, many images do not support secret injection automatically via Docker Swarm. This project addresses that by acting as an **intermediate entrypoint** that:
1. Scans all environment variables.
2. If an environment variable ends with `_SECRET`, it looks for the corresponding secret file mounted in the container.
3. If the secret exists, it loads the content of the secret into the environment variable without the `_SECRET` suffix.

For example, if you have:
- An environment variable `DB_PASSWORD_SECRET` in your container,
- A mounted secret at `/run/secrets/DB_PASSWORD`,

The script will automatically set the environment variable `DB_PASSWORD` with the content of `/run/secrets/DB_PASSWORD`.

## Requirements

- Docker Swarm enabled on the system.
- Docker version 1.13 or higher.
- Docker image that does not natively support Docker Swarm secrets.

## Usage

### 1. Build the Docker Image

Start by building the custom Docker image based on your existing image. This layer will add the secret support functionality.

```bash
docker build -t my_image_with_secrets .
```

### 2. Run the Container with Secrets

When running the container, specify the secrets to be mounted as environment variables. Docker Swarm will automatically mount secrets to `/run/secrets/<secret_name>` inside the container.

Example:

```bash
docker service create \
  --name my_service_with_secrets \
  --secret DB_PASSWORD \
  --secret API_KEY \
  my_image_with_secrets
```

In the above example:
- `DB_PASSWORD` and `API_KEY` are secret names managed by Docker Swarm.
- The environment variable `DB_PASSWORD_SECRET` will be converted to `DB_PASSWORD` with the value of the `/run/secrets/DB_PASSWORD` secret file.
- The environment variable `API_KEY_SECRET` will be converted to `API_KEY` with the value of the `/run/secrets/API_KEY` secret file.

### 3. Dockerfile Example

Here is an example of a `Dockerfile` using this layer:

```dockerfile
# Start from an existing image (e.g., python:3.11-slim)
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the entrypoint script that handles secret injection
COPY entrypoint.py /app/

# Make the script executable
RUN chmod +x /app/entrypoint.py

# Override the entrypoint to run the custom script first
ENTRYPOINT ["sh", "-c", "python3 /app/entrypoint.py && exec ${0} ${@}"]

# Default command to run the application (e.g., python app.py)
CMD ["python3", "app.py"]
```

### 4. Example `entrypoint.py` Script

Your `entrypoint.py` script (or similar) should include logic that detects and processes the `_SECRET` variables, as shown in the previous Dockerfile example.

---

## How to Contribute

We welcome contributions to improve the project! If you find a bug or have an idea for a new feature, feel free to open an issue or submit a pull request.

### Steps to contribute:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Implement your changes.
4. Open a pull request with a description of your changes.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

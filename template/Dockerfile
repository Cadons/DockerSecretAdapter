# Start from the existing Docker image
FROM docmost/docmost:latest

# Set the working directory inside the container
WORKDIR /app

# Copy your custom entrypoint script
COPY entrypoint.py /starter/
#install python using the installed package manager (apk, apt, pacman, ...) 
#If it is already installed remove the following 2 lines
#change user
USER root
RUN apk update
RUN apk add python3

# Make the script executable (if necessary)
RUN chmod +x /starter/entrypoint.py
USER node
# Override the entrypoint to run your custom script first
ENTRYPOINT ["sh", "-c", "python3 /starter/entrypoint.py&& source configure_secrets.sh && pnpm start"]

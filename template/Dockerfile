# Start from the existing Docker image
FROM existing-image:latest  # Replace with the actual image name

# Set the working directory inside the container
WORKDIR /app

# Copy your custom entrypoint script
COPY entrypoint.py /starter/
#install python using the installed package manager (apk, apt, pacman, ...) 
#If it is already installed remove the following 2 lines
RUN apt update
RUN apt install python3

# Make the script executable (if necessary)
RUN chmod +x /starter/entrypoint.py

# Override the entrypoint to run your custom script first
ENTRYPOINT ["sh", "-c", "python3 /starter/entrypoint.py && exec ${0} ${@}"]

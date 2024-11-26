import os

def process_secrets():
    """
    Process environment variables ending with _SECRET.
    For each, read the file at the path specified by the variable's value
    and export a new variable without the _SECRET suffix containing the secret content.
    Writes these environment variables to a .env file.
    """
    with open("configure_secrets.sh", "w") as env_file:
        for key, value in os.environ.items():
            env_file.write("#!/bin/bash")
            env_file.write("\n")
            env_file.write("set -e")
            env_file.write("\n")
            env_file.write("echo 'configuring enviroment'\n")
            if key.endswith("_SECRET"):
                # Derive the new variable name by removing "_SECRET"
                base_var_name = key[:-7]

                # Check if the value points to a valid file
                if os.path.isfile(value):
                    try:
                        # Read the content of the secret file
                        with open(value, "r") as secret_file:
                            secret_value = secret_file.read().strip()

                        # Write the new variable to the .env file
                        env_file.write(f'export {base_var_name}="{secret_value}";\n')

                        print(f"Written {base_var_name} to configure_secrets.sh from secret {key} ({value})")
                    except Exception as e:
                        print(f"Error reading secret file {value} for {key}: {e}")
                else:
                    print(f"Warning: Secret file {value} not found for {key}")

# Process secrets and write to .env file
process_secrets()

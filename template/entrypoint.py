import os

def process_secrets():
    """
    Process environment variables ending with _SECRET.
    For each, read the file at the path specified by the variable's value
    and export a new variable without the _SECRET suffix containing the secret content.
    """
    for key, value in os.environ.items():
        if key.endswith("_SECRET"):
            # Derive the new variable name by removing "_SECRET"
            base_var_name = key[:-7]

            # Check if the value points to a valid file
            if os.path.isfile(value):
                try:
                    # Read the content of the secret file
                    with open(value, "r") as secret_file:
                        secret_value = secret_file.read().strip()

                    # Export the new environment variable
                    os.environ[base_var_name] = secret_value
                    print(f"Exported {base_var_name} from secret {key} ({value})")
                except Exception as e:
                    print(f"Error reading secret file {value} for {key}: {e}")
            else:
                print(f"Warning: Secret file {value} not found for {key}")

# Process secrets
process_secrets()

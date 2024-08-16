import subprocess

def run_ollama_command(command):
    try:
        # Start the process
        process = subprocess.Popen(
            command,
            shell=True,                   # Use shell=True to allow command as a string
            stdout=subprocess.PIPE,      # Redirect standard output
            stderr=subprocess.PIPE,      # Redirect standard error
            text=True                     # Return output as a string (text mode)
        )
        
        # Wait for the process to complete
        stdout, stderr = process.communicate()

        # Check if the command was successful
        if process.returncode == 0:
            # Process the output to remove the first 2 lines
            output_lines = stdout.strip().split('\n')
            if len(output_lines) > 2:
                # Return the output excluding the first 2 lines
                return '\n'.join(output_lines[2:])
            else:
                # Return an empty string if there are fewer than 3 lines
                return ""
        else:
            return f"Error: {stderr.strip()}"  # Return the error if any

    except Exception as e:
        return f"An error occurred: {e}"

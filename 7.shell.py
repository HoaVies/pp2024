import os
import subprocess

def execute_command(command, input_file=None, output_file=None):
    try:
        if input_file and output_file:
            with open(input_file, 'r') as in_f, open(output_file, 'w') as out_f:
                process = subprocess.Popen(command.split(), stdin=in_f, stdout=out_f, stderr=subprocess.PIPE)
        elif input_file:
            with open(input_file, 'r') as f:
                process = subprocess.Popen(command.split(), stdin=f, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        elif output_file:
            with open(output_file, 'w') as f:
                process = subprocess.Popen(command.split(), stdout=f, stderr=subprocess.PIPE)
        else:
            process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        output, error = process.communicate()
        if error:
            print(f"Error: {error.decode()}")
            return None
        return output.decode()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        
def main():
    """The main loop of the shell."""

    while True:
        prompt = "$ "
        command = input(prompt)
        if command == 'exit':
            break

        # Check for input and output redirection
        parts = command.split('>')
        if len(parts) == 2:
            command = parts[0].strip()
            output_file = parts[1].strip()
            output = execute_command(command, output_file=output_file)
        elif len(parts) > 2:
            print("Error: Invalid redirection syntax.")
            continue

        parts = command.split('<')
        if len(parts) == 2:
            command = parts[0].strip()
            input_file = parts[1].strip()
            output = execute_command(command, input_file=input_file)
        elif len(parts) > 2:
            print("Error: Invalid redirection syntax.")
            continue

        if output:
            print(output)

if __name__ == "__main__":
    main()
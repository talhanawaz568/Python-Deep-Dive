import subprocess

result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
print("Standard Output:")
print(result.stdout)
print("Standard Error (if any):")
print(result.stderr)


if result.returncode == 0:
	print("Command executed successfully")
else:
	print("Command failed with exit code:", result.returncode)

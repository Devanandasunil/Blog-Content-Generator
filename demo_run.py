import subprocess
import sys

# Run main.py with sample input
input_data = """Artificial Intelligence
Tech Enthusiasts
professional
"""

process = subprocess.Popen(
    [sys.executable, "main.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

stdout, stderr = process.communicate(input=input_data, timeout=120)
print(stdout)
if stderr:
    print("STDERR:", stderr)

from pathlib import Path
content = Path("index.html").read_text()
assert "Hello from Kubernetes!" in content
print("================================")
print("Test Passed")
print("================================")

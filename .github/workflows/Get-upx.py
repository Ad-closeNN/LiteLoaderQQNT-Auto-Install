import subprocess

command = 'curl -s https://api.github.com/repos/upx/upx/releases/latest | findstr "browser_download_url" | findstr "win64.zip"'
result = subprocess.run(command, shell=True, capture_output=True, text=True)

if result.stdout:
    url = result.stdout.split('"')[3]
    with open("url", "w") as f:
        f.write(url)
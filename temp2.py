import subprocess

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout, stderr

def test_temp():
    stdout, stderr = run_command("python temp.py")
    assert not stderr, stderr.decode()
    assert b"Traceback" not in stdout, stdout.decode()
    assert b"File" not in stdout, stdout.decode()
    assert b"Error" not in stdout, stdout.decode()
    assert b"Exception" not in stdout, stdout.decode()
    assert b"Warning" not in stdout, stdout.decode()
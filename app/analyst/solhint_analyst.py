import subprocess

from config import data_dir


def solhint_analyst(file_path):
    cmd = 'solhint ' + file_path
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    out = out.decode('utf-8')
    err = err.decode('utf-8')

    if out != '':
        save_output('solhint_output.txt', out)

    if err != '':
        save_output('solhint_error.txt', err)

    return out, err


def save_output(file_path, output):
    with open(data_dir(file_path), 'w') as f:
        f.write(output)
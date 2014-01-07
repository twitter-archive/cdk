import subprocess

def check_output(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    output, unused_err = process.communicate()
    retcode = process.poll()
    if retcode:
        error = subprocess.CalledProcessError(retcode, cmd)
        error.output = output
        raise error
    return output

import subprocess
from pexpect import popen_spawn


user = 'ankurr2011@gmail.com'
password = 'Anmarch@2018'

cmd = "cd C:\\git-test"
returned_value = subprocess.call(cmd, shell=True)  # returns the exit code in unix

cmd = "git add ." 
subprocess.call(cmd, shell=True)

cmd = 'git commit -m "python project update"'
subprocess.call(cmd, shell=True)

# cmd = "git remote add origin https://github.com/ankur9718/Test.git"
# subprocess.call(cmd, shell=True)

cmd = "git remote set-url origin https://github.com/ankur9718/Test.git"
subprocess.call(cmd, shell=True)

cmd = "git push origin master "
child_process = popen_spawn.PopenSpawn(cmd)
# child_process.expect('User')
child_process.sendline(user)
# child_process.expect('Password')
child_process.sendline(password)
print('returned value:', returned_value)

print('end of commands')
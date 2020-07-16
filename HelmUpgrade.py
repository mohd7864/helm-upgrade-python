import re
import shutil
from subprocess import run, call, PIPE


class Helm:

  def __init__(self, debug=False):
    self.dbg = debug

    # test if helm is in PATH
    if shutil.which('helm') is None:
      print('Helm is not installed')
      return

    # test Helm version
    p = run(["helm", "version"], check=True, stdout=PIPE).stdout
    m = re.search(r'"v(\d+?).(\d+?).(\d+?)-?[^"]*"', str(p))
    if m:
      major = m.group(1)
      minor = m.group(2)
      patch = m.group(3)
    else:
      print('No regex version available')
      return

    if int(major) < 3:
      print('This package only work with Helm 3.x.y')

    print("Using Helm Major: " + major + ". Minor: " + minor + ". Patch: " + patch)
    
  def upgrade(self, name, path, namespace='default', wait=False):

    # MANDATORY : all helm upgrade command must start with
    command = [
      "helm",
      "upgrade",
      "--install"
    ]

    if wait:
      command.append("--wait")

    # MANDATORY : these two arguments must be the last
    command.append(name)
    command.append(path)
    print(command)
    run(["helm","repo", "update"])
    p = run(command)
    print(str(p))
    # call the command locally
    #if self.dbg:
    #  print(command)
    #else:
      # we launch command
    #  p = run(command, check=True, stdout=PIPE).stdout

      # search if answer is an error of repo update
    #  m = re.search('`helm repo update`', str(p))
    #  if m:
        # update the repo and launch command again
    #    run(["helm","repo", "update"])
    #    p = run(command, check=True, stdout=PIPE).stdout

    #  # print final output
    #  print(str(p))

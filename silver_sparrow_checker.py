import sys,os,subprocess

path = os.path.expanduser('~')

print("Silver Sparrow infection checker")

architecture = subprocess.check_output(['uname','-m'])
print("Architecture is {}".format(architecture.decode('utf-8')).strip('\n'))

files = ["{}/Library/Application Support/agent_updater/agent.sh","{}/Library/Launchagents/agent.plist",
         "{}/Library/Launchagents/init_agent.plist","{}/Library/Application Support/verx_updater/verx.sh",
         "{}/Library/Application Support/verx_updater/verx.plist","{}/Library/Application Support/verx_updater/init_verx.plist"] 

files = [x.format(path) for x in files]

temp_files = ["/tmp/agent.sh","/tmp/version.json","/tmp/version.plist","/tmp/agent","/tmp/verx"]

immunity_file = "{}/Library/._insu".format(path)
flag = False

for file in files:
    if os.path.exists(file):
        print('WARNING file exists at {}'.format(file))
        flag = True

for file in temp_files:
    if os.path.exists(file):
        print('WARNING file exists at {}'.format(file))
        flag = True

if not os.path.exists(immunity_file):
    with open(immunity_file, mode='a'): 
        print('Imunnity file created')
else: print('Imunnity file exists')

if flag == True:
    print('SYSTEM INFECTED')
else:
    print('No infection found')

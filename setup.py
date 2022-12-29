import os
import json 
import subprocess

years = ('2016', '2018', '2019', '2020')
files = ('.gitignore', 'tsconfig.json', 'cookie.txt')
with open('/Users/nickwarters/dev/aoc-template/package.json') as file:
    templatePkgJson = json.loads(file.read())
    print(templatePkgJson)

os.chdir('/Users/nickwarters/dev/')

print(os.getcwd())
for year in years:
    subprocess.run(['gh', 'repo', 'clone', f'aoc-{year}'])
    os.chdir(f'/Users/nickwarters/dev/aoc-{year}')
    subprocess.run(['npm', 'init', '-y'])
    with open(f'/Users/nickwarters/dev/aoc-{year}/package.json', 'r+') as file:
        pkgJson = json.loads(file.read())
        pkgJson['scripts'] = templatePkgJson['scripts']
        pkgJson['type'] = templatePkgJson['type']
        pkgJson['dependencies'] = templatePkgJson['dependencies']
        pkgJson['devDependencies'] = templatePkgJson['devDependencies']
        file.seek(0)
        file.write(json.dumps(pkgJson))
        file.truncate()

    subprocess.run(['npm', 'i'])

# copy the config files and cookie file 
    for fileName in files:
        subprocess.run(['cp', f'/Users/nickwarters/dev/aoc-template/{fileName}', f'/Users/nickwarters/dev/aoc-{year}/{fileName}'])

    os.mkdir('src')
    subprocess.run(['cp', '-a', '/Users/nickwarters/dev/aoc-template/src/utils', f'/Users/nickwarters/dev/aoc-{year}/src/utils'])
    subprocess.run(['cp', '-a', '/Users/nickwarters/dev/aoc-template/src/00', f'/Users/nickwarters/dev/aoc-{year}/src/00'])
    for day in range(25):
        dayStr = f'{day + 1}'.zfill(2)
        subprocess.run(['cp', '-a', f'/Users/nickwarters/dev/aoc-template/src/{dayStr}', f'/Users/nickwarters/dev/aoc-{year}/src/{dayStr}'])
        subprocess.run(['npm', 'run', 'downloadInput', f'{day + 1}'])

    os.chdir('/Users/nickwarters/dev/')

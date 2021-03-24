from pathlib import Path

# Absolute path
#c:\Program File\Microsoft
#/usr/local/bin
# Relatice path

path = Path()
for file in path.glob('*'):
    print(file)
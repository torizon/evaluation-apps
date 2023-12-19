import os

root_dir = os.getcwd()
readme_files = []
too_large_files = []

def walk(dir):
    for dirpath, _, filenames in os.walk(dir):
        for filename in filenames:
            if filename.lower() == 'readme.md':
                readme_files.append(os.path.join(dirpath, filename))

walk(root_dir)

max_size_in_bytes = 1024  # Set your maximum size in bytes

# find large files
for readme_file in readme_files:
    file_size_in_bytes = os.path.getsize(readme_file)
    if file_size_in_bytes > max_size_in_bytes:
        too_large_files.append(readme_file)

if too_large_files:
    print(f'Error: at least one file size exceeds {max_size_in_bytes} bytes:')
    print(too_large_files)
    exit(1)
else:
    print('README size check passed.')
    exit(0)

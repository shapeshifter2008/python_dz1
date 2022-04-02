import os
from random import randint
from shutil import copy

project_dir = './my_project'

def create_folder(project_dir, dir_path):
    if not os.path.exists(f'{project_dir}/{dir_path}'):
        os.mkdir(f'{project_dir}/{dir_path}')
    return True

for root, dirs, files in os.walk(project_dir):
    if f'{project_dir}/templates' in root:
        continue

    for file in files:
        if '.html' in file:
            base_name = os.path.basename(root)

            create_folder(project_dir, 'templates')
            create_folder(project_dir, f'templates/{base_name}')

            copy_name = file
            while True:
                if os.path.exists(f'{project_dir}/templates/{base_name}/{file}'):
                    copy_name = f'{randint(1, 1000)}_{file}'
                    break
                else:
                    break

            print('Создан файл: ', f'{project_dir}/templates/{base_name}/{copy_name}')
            copy(f'{root}/{file}', f'{project_dir}/templates/{base_name}/{copy_name}')
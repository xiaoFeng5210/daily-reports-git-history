import os
import subprocess
from datetime import datetime

work_dir = '/Users/xiaofeng/Documents/work/lebai'

# 输出目录
output_file = 'git_history.txt'


def get_git_history(project_path):
  try:
    result = subprocess.run(
            ['git', 'log', '--since=midnight', '--pretty=format:%h %ad | %s%d [%an]', '--date=short'],
            cwd=project_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
          )
    if result.returncode == 0:
        return result.stdout
    else:
        return f"Error getting git history for {project_path}: {result.stderr}"

  except Exception as e:
    print(f'Error: {e}')

def main():
  with open(output_file, 'w') as f:
    for project in os.listdir(work_dir):
      # 拿到每个项目的路径
      project_path = os.path.join(work_dir, project)
      if (os.path.isdir(project_path) and ('.' not in project)):
        f.write(f'Project: {project}\n')
        f.write(get_git_history(project_path))
        f.write('\n\n')

if __name__ == '__main__':
  main()

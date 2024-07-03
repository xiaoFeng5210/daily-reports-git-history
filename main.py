import os

work_dir = '/Users/xiaofeng/Documents/work/lebai'

# 输出目录
output_file = 'git_history.txt'

def main():
  with open(output_file, 'w') as f:
    for project in os.listdir(work_dir):
      # 拿到每个项目的路径
      project_path = os.path.join(work_dir, project)
      if (os.path.isdir(project_path) and ('.' not in project)):
        f.write(f'Project: {project}\n')


if __name__ == '__main__':
  main()

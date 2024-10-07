"""Post-project generation hooks"""

if __name__ == '__main__':
    """Initialize a git repository."""

    import subprocess
    subprocess.call(('git', 'init'))
    subprocess.call(('qlot', 'init'))
    subprocess.call(('qlot', 'install'))
    subprocess.call(('qlot', 'add', 'dist', 'http://dist.ultralisp.org/'))
    subprocess.call(('qlot', 'update'))

    print("Project {{ cookiecutter.project_name }} created succesfully.")

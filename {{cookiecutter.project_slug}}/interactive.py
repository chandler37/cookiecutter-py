# This file is meant to be used as in `env PYTHONSTARTUP=interactive.py ipython`

from {{cookiecutter.project_slug}} import cat

print("""The PYTHONSTARTUP environment variable caused us to load and execute
interactive.py. You may now type things like the following:

cat.read_file_lines("LICENSE")
dir(cat)
help(cat)

That's because we've run this:

from {{cookiecutter.project_slug}} import cat

Enjoy! Remember, anything you do in an automated test will not only work today,
but work tomorrow as well. So take what you learn here and write new tests.
""")

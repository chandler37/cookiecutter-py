# {{cookiecutter.project_slug}}

This is a repository to help you learn Python, to explore an idea, or to write a full-fledged pypi package.

Automated testing is important, and a command-line interface (CLI) is often a
great way to share your idea, so this template helps you do both.

## Committing

Essentially you want https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow/

- git checkout master
- git pull --ff-only
- git checkout origin/master -b featurebranch
- git add newfile
- git add modifiedfile
- git commit
- git status
- verify that there are no files you forgot to commit
- git push origin HEAD
- use the URL it printed to create the pull request and merge it
- back to step 1!


## Installing (but not developing)

TODO: Make setup.py work so people can install this. You could even put this on
pypi; the directory structure is adequate.

[Homebrew](https://brew.sh/) is required.


## Developing

Run tests via `make test`

Run ipython via `make shell`

Or run the command-line interface:

```sh
$ (source venv/bin/activate && python {{cookiecutter.project_slug}}-runner.py cat .gitignore)
__pycache__
*.pyc
.DS_Store
/venv
.cache
```


### Adding a third-party package as a dependency

If you want a https://pypi.org/ package, e.g. numpy, just add it to requirements.txt and then run `make test`:

- `echo "numpy" >> requirements.txt && make test`
- If it works, you might want to freeze the version and the version of any
  transitive dependencies that were brought in via `make unfreezeplus` but it
  will perform some upgrades as well that you might want to undo.

You may have already installed the package globally on your system, but that's
insufficient because {{cookiecutter.project_slug}} uses a virtual environment courtesy of the
`venv` Python standard library. Here you must be explicit about your
dependencies, but you can use exactly the versions that you want and you can
peacefully coexist with other projects that use different versions.

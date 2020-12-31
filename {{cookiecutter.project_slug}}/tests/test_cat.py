from {{cookiecutter.project_slug}} import cat
import pytest


def test_create_multiline_file(tmpdir, capsys):
    contents = r"""Not a bad fie am I??!
Just for fun
\n
the above is a new line character"""
    p = tmpdir.mkdir("sub").join("hello.txt")
    p.write(contents)
    cat.read_file_lines(str(p))
    out, err = capsys.readouterr()
    assert out == contents + '\n'


def test_create_empty_string_file(tmpdir, capsys):
    contents = ''
    p = tmpdir.mkdir("sub").join("none.txt")
    p.write(contents)
    cat.read_file_lines(str(p))
    out, err = capsys.readouterr()
    assert out == ''
    assert err == ''


def test_create_single_line_file(tmpdir, capsys):
    contents = "Not a bad fie am I??!"
    p = tmpdir.mkdir("sub").join("boo.txt")
    p.write(contents)
    cat.read_file_lines(str(p))
    out, err = capsys.readouterr()
    assert out == '%s\n' % contents
    assert out == '{}\n'.format(contents)
    assert err == ''


def test_nonexistant_file():
    with pytest.raises(IOError) as excinfo:
        cat.read_file_lines('/nonexistant_file')
    assert str(excinfo.value) == "[Errno 2] No such file or directory: '/nonexistant_file'"

# -*- coding: utf-8 -*-


"""{{cookiecutter.project_slug}}.cat: cat(1) basic reimplementation -- reads a file and prints it to standard output"""


def read_file_lines(pathname):
    """ Raises IOError"""
    with open(pathname, 'r') as f:  # 'rb' would be binary; 'rt' would be text; which is the default? hmmm...
        for line in f:
            print(line.rstrip())


# ReadLines2
#         f = open(args.path, 'r')
#         try:
#             for line in f:
#                 print(line.rstrip())
#         finally:
#             f.close()
# Please note 'try:... finally:' works the same way as 'with...as' helps in closing out the files that were opened


import os
import sys

def is_package(path):
    for name in os.listdir(path):
        if name  in ('autoload.php'):
            return False
    return True

def directory_walk(basepath,ext,packages=None):
    for dirpath, dirnames, filenames in os.walk(basepath):
        for dirname in list(dirnames):
            """print dirname"""

            if dirname[0] == '.':
                dirnames.remove(dirname)
                continue

            if is_package(dirpath) and filenames:
                pkg_name = dirpath[len(basepath) + len(os.sep):].replace(',','.')
                if packages and pkg_name not in packages:
                    continue

                filenames = filter(lambda x:x.startswith('wp-') and x.endswith(ext),filenames)

                for name in filenames:
                        yield name

this_dir_path = os.path.abspath(os.path.dirname(__file__))
for fname in directory_walk(this_dir_path,'.php'):
    print fname





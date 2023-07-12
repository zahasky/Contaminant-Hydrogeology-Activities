import platform
import sys
from packaging.version import parse as version_parse

if version_parse(platform.python_version()) < version_parse('3.8'):
    print('[FAIL] We recommend Python 3.8 or newer but'
          ' found version %s' % (sys.version))
else:
    print('[OK] Your Python version is %s' % (platform.python_version()))


def get_packages(pkgs):
    versions = []
    for p in pkgs:
        try:
            imported = __import__(p)
            try:
                versions.append(imported.__version__)
            except AttributeError:
                try:
                    versions.append(imported.version)
                except AttributeError:
                    try:
                        versions.append(imported.version_info)
                    except AttributeError:
                        versions.append('0.0')
        except ImportError:
            print(f'[FAIL]: {p} is not installed and/or cannot be imported.')
            versions.append('N/A')
    return versions


def check_packages(d):

    versions = get_packages(d.keys())

    for (pkg_name, suggested_ver), actual_ver in zip(d.items(), versions):
        if actual_ver == 'N/A':
            continue
        actual_ver, suggested_ver = version_parse(actual_ver), version_parse(suggested_ver)
        if actual_ver < suggested_ver:
            print(f'[FAIL] {pkg_name} {actual_ver}, please upgrade to >= {suggested_ver}')
        else:
            print(f'[OK] {pkg_name} {actual_ver}')


if __name__ == '__main__':
    d = {
        'numpy': '1.24.3',
        'scipy': '1.10.1',
        'pandas': '2.0.2',
        'matplotlib': '3.7.1',
        'flopy': '3.3.0',
        'gstools': '1.3.0',
        'jupyterlab': '4.0',
        'ipywidgets': '8.0.6'
    }
    check_packages(d)

from glob import glob
import platform
import subprocess
import os
import platform
import sys

is_windows = platform.system() == "Windows"
exe_suffix = ".exe" if is_windows else ""


def find_script_dirs():
    """Search for 'scripts' subdirectory that Python can use."""
    script_dirs = []
    for path in sys.path:
        # print("Path:", path)
        path_parent = os.path.dirname(path)
        script_dir = os.path.join(path_parent, "scripts")
        # print(script_dir)
        if not os.path.isdir(script_dir):
            continue
        elif script_dir in script_dirs:
            continue
        else:
            script_dirs.append(script_dir)

    assert len(script_dirs) > 0

    path_sep = ";" if is_windows else ":"
    path_dirs = os.environ["PATH"].split(path_sep)
    script_dirs += path_dirs

    return script_dirs


def find_script(script):
    script += exe_suffix
    script_dirs = find_script_dirs()
    for script_dir in script_dirs:
        script_filepath = os.path.join(script_dir, script)
        # print(script_filepath)
        if os.path.isfile(script_filepath):
            return script_filepath

    assert "Script '%s' not found in %s" % (script, script_dirs)


uic = find_script("pyside2-uic")

print("Generate Python code from .ui files:")
py_filepaths = []
for ui in glob("*.ui"):
    filename = os.path.splitext(ui)[0]
    movepath = ui_path = "ui_python"
    _py_filepath = "ui_%s.py" % filename
    py_filepath = os.path.join("..", movepath, _py_filepath)
    py_filepaths.append(py_filepath)
    print("Generate %s..." % filename, end="", flush=True)

    if os.path.isfile(py_filepath):
        ui_mtime = os.stat(ui).st_mtime
        py_mtime = os.stat(py_filepath).st_mtime
        if py_mtime > ui_mtime:
            print("Not necessary")
            continue

    subprocess.run([uic, "-o", py_filepath, ui], check=True)
    print("OK")

# Delete unused formerly generated files
for py_filepath in glob("ui_*.py"):
    if py_filepath not in py_filepaths:
        print("Remove %s..." % py_filepath, end="", flush=True)
        os.remove(py_filepath)
        print("OK")

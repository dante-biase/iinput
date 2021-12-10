import os
import re
import platform
import getpass

import utils as __utils


def yn(prompt, default=None):
    inp = None
    while inp not in ['y', 'n']:
        inp = str(input(f"{prompt} [y/n]: ")).strip().lower()
        if not inp and default is not None:
            return default
    return inp


def value(prompt, allowed_types=[str], default=''):
    while True:
        inp = str(input(f"{prompt}: ")).strip()
        if not inp and default is not None:
            return default

        inp_type = __utils.interpret_type(inp)
        if inp_type in allowed_types:
            return inp_type(inp)
        elif inp and str in allowed_types:
            return inp


def values(prompt, delimiter=',', allowed_types=[str], default=[]):
    inp = items = None
    while not (inp and items):
        inp = str(input(f"{prompt}: ")).strip()
        if not inp and default is not None:
            return default

        items = __utils.split_ws(inp, delimiter)
        items = __utils.auto_cast(items, allowed_types)
    return items


def match_value(prompt, target, max_attempts=-1):
    target = str(target)
    attempts = 0
    inp = None
    while inp != target and attempts != max_attempts:
        inp = str(input(f"{prompt}: "))
        attempts += 1
    return attempts != max_attempts


def match_values(prompt, targets, max_attempts=-1, delimiter=','):
    targets = [str(v) for v in targets]
    attempts = 0
    inps = []
    while sorted(inps) != sorted(targets) and attempts != max_attempts:
        inp = str(input(f"{prompt}: "))
        inps = __utils.split_ws(inp, delimiter)
        attempts += 1
    return attempts != max_attempts


def boolean(prompt, default=None):
    while True:
        inp = str(input(f"{prompt}: ")).strip()
        if not inp and default is not None:
            return default
        try:
            inp = bool(inp)
            return inp
        except ValueError:
            pass


def number(prompt, default=None):
    while True:
        inp = str(input(f"{prompt}: ")).strip()
        if not inp and default is not None:
            return default
        cast = float if '.' in inp else int
        try:
            inp = cast(inp)
            return inp
        except ValueError:
            pass


def integer(prompt, default=None):
    while True:
        inp = str(input(f"{prompt}: ")).strip()
        if not inp and default is not None:
            return default
        try:
            inp = int(inp)
            return inp
        except ValueError:
            pass


def floating_point(prompt, default=None):
    while True:
        inp = str(input(f"{prompt}: ")).strip()
        if not inp and default is not None:
            return default
        try:
            inp = float(inp)
            return inp
        except ValueError:
            pass


def character(prompt, default=None):
    inp = ''
    while not __utils.ischar(inp):
        inp = str(input(f"{prompt}: "))
        if not inp and default is not None:
            return default
    return inp


def string(prompt, default=''):
    inp = ''
    while not inp:
        inp = str(input(f"{prompt}: "))
        if not inp and default is not None:
            return default
    return inp


def alpha(prompt, default=None):
    inp = ''
    while not inp.isalpha():
        inp = str(input(f"{prompt}: ")).strip()
        if not inp and default is not None:
            return default
    return inp


def alphanumeric(prompt, default=None):
    inp = ''
    while not inp.isalnum():
        inp = str(input(f"{prompt}: ")).strip()
        if not inp and default is not None:
            return default
    return inp


def line(prompt, default=''):
    inp = None
    while not inp:
        inp = str(input(f"{prompt}: ")).strip()
        if not inp and default is not None:
            return default
    return inp


def lines(prompt):
    print(f"{prompt}: ")
    lines = []
    while True:
        try:
            l = input()
            l = str(l).strip()
            lines.append(l)
        except EOFError:
            return lines


def selection(menu_options, header="menu", prompt="enter selection", default=None):
    if header:
        print(header)
    for key, value in menu_options.items():
        print(f"\t[{key}]: {value}")
    print()

    menu_options = {str(k): v for k, v in menu_options.items()}
    selected_key = None
    while selected_key not in menu_options:
        selected_key = str(input(f"{prompt}> ")).strip()
        if not selected_key and default is not None:
            return default
    return selected_key


def multiselection(menu_options, header="menu", prompt="enter selection", delimiter=',', default=None):
    if header:
        print(header)
    for key, value in menu_options.items():
        print(f"\t[{key}]: {value}")
    print()

    menu_options = {str(k): v for k, v in menu_options.items()}
    selected_keys = []
    while not selected_keys or all(s not in menu_options.keys() for s in selected_keys):
        inp = str(input(f"{prompt}> "))
        selected_keys = __utils.split_ws(inp, delimiter)
        if not selected_keys and default is not None:
            return default
    return selected_keys


def email(prompt, default=''):
    email = None
    while not email:
        inp = str(input(f"{prompt}: ")).strip()
        if not inp and default is not None:
            return default
        email = re.match(r"^[^@]+@[^@]+\.[^@]+$", inp)
    return email.group()


def password(prompt, default=''):
    pwd = None
    while not pwd:
        pwd = getpass.getpass(prompt=f"{prompt}: ")
        if not pwd and default is not None:
            return default
    return pwd


def match_password(prompt, target, max_attempts=-1):
    target = str(target)
    attempts = 0
    pwd = None
    while pwd != target and attempts != max_attempts:
        pwd = getpass.getpass(prompt=f"{prompt}: ")
        attempts += 1
    return attempts != max_attempts


def regex(prompt, r, flags, default=None):
    match = None
    while not match:
        inp = str(input(f"{prompt}: "))
        if not inp and default is not None:
            return default
        match = re.match(r, inp, flags=flags)
    return match


def wait_for_key_press(key, prompt="press \'{}\' to continue..."):
    prompt = prompt.format(key)
    inp = None
    while inp != key:
        inp = str(input(f"{prompt}: "))


def wait_for_some_key_press(keys, prompt="press \'{}\' to continue..."):
    prompt = prompt.format(keys)
    inp = None
    while inp not in keys:
        inp = str(input(f"{prompt}: "))


def wait_for_any_key_press(prompt="press any key to continue..."):
    if platform.system() == "Windows":
        print(prompt)
        os.system("pause")
    else:
        os.system(f"read -s -n 1 -p \"{prompt}\"")


def wait_for_enter(prompt="press ENTER to continue..."):
    input(prompt)
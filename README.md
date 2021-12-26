
# iinput

iinput is a simple, extended version of Python's standard input that provides numerous functions for acquiring input of specific type(s), value(s), patterns, and constraints.

# features
- yes or no input
- specific type input
- single and multi-value input with automatic type casting
- single and multi-selection menu input
- single and multi-line input
- single and multi-target matching input
- email and password input
- pattern matched input
- wait events for any, specific, or single key press
- empty or default input functionality

# dependencies
- [keyboard](https://github.com/boppreh/keyboard)

# requirements

- Python 3.6^

# install

```bash
$ pip3 install iinput
```
| DESCRIPTION                                       | FUNCTION                                                                                                                             | RETURN  |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|--------------|
| equivalent to standard input                               | _(prompt: str = '')                                                                                                 | Any          |
| get yes or no input                               | yn(prompt: str, default: Any = None)                                                                                                 | str          |
| get single value of specified type                | value(prompt: str, allowed_types: List[type] = [str], default: str = '')                                                             | Any          |
| get multiple values of specified type(s)          | values(prompt: str, delimiter: str = ',', allowed_types: List[type] = [str], default: list = [])                                     | list         |
| wait for input to match some target               | match_value (prompt: str, target: str, max_attempts: int = -1)                                                                       | bool         |
| wait for input to match some target(s)            | match_values(prompt: str, targets: list, delimiter: str = ',', max_attempts: int = -1)                                               | bool         |
| get boolean input                                 | boolean(prompt: str, default: Any = None)                                                                                            | bool         |
| get number input                                  | number(prompt: str, default: Any = None)                                                                                             | int or float |
| get integer input                                 | integer(prompt: str, default: Any = None)                                                                                            | int          |
| get floating point input                          | floating_point(prompt: str, default: Any = None)                                                                                     | float        |
| get character input (no strip)                              | character (prompt: str, default: Any = None)                                                                                         | str          |
| get string input                                  | string (prompt: str, default: str = '')                                                                                              | str          |
| get alpha input                                   | alpha(prompt: str, default: Any = None)                                                                                              | str          |
| get alphanumeric input                            | alphanumeric(prompt: str, default: Any = None)                                                                                       | str          |
| get entire line input (no strip)                  | line(prompt: str, default: str = '')                                                                                                 | str          |
| get line inputs until empty (no strip)            | lines (prompt: str)                                                                                                                  | List[str]    |
| print menu, get selected option and its value     | selection(menu_options: dict, header: str = "menu", prompt: str = "enter selection", default: Any = None)                            | str          |
| print menu, get selected options and their values | multiselection(menu_options: dict, header: str = "menu", prompt: str = "enter selection", delimiter: str = ',', default: Any = None) | List[str]    |
| get email input                                   | email(prompt: str, default: str = '')                                                                                                | str          |
| get password input (discrete)                     | password (prompt: str, default: str = '')                                                                                            | str          |
| wait for input to match target (discrete)         | match_password(prompt: str, target: str, max_attempts: int = -1)                                                                     | bool         |
| get pattern matched input                         | regex(prompt: str, r: str, flags: int = 0, default: Any = None)                                                                      | Match[str]   |
| wait for a specific key press event               | wait_for_key_press(key: str, prompt: str = "press '{}' to continue...")                                                              | None         |
| wait for any select key press event               | wait_for_some_key_press (keys: List[str], prompt: str = "press {} to continue...")                                                   | None         |
| wait for any key press event                      | wait_for_any_key_press(prompt: str = "press any key to continue...")                                                                 | None         |
| wait for "enter" key press event                  | wait_for_enter(prompt: str = "press ENTER to continue...")                                                                           | None         |

## stripping
- all input is stripped unless specified otherwise

## empty input
- empty input is **whitespace** input
- **to enable empty input returns, set default = ''**

## default
- returned when input is whitespace and default is **not** None

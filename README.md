# FontAwesome Python Wrapper

This module allows to insert FontAwesome Unicode characters in Python 2/3 in a human readable way.

## Usage

First, import the `FontAwesome` object instance:

```pycon
>>> from fontawesome import fa
```

### Using dict notation (getitem)

`fa` inherits from `dict`, so you can use all `dict` methods.

```pycon
>>> print(fa["font-awesome"], "FontAwesome is Awesome", fa["fort-awesome"])
 FontAwesome is Awesome 
```

### Using object attributes notation (getattr)

`fa` implements custom `__getattr__` and `__dir__` methods, so you can use icon names as normal attributes (replacing `-` with `_` as it's an illegal character).

```pycon
>>> print(fa.font_awesome, "FontAwesome is Awesome", fa.fort_awesome)
 FontAwesome is Awesome 
```

### Using string formatting

`fa` also implements a convenient `format` method, based on `re`. When a string is passed, it will replace `{fa-icon}` with the curresponding icon, if found.

```pycon
>>> print(fa.format("{fa-font-awesome} FontAwesome is Awesome {fa-fort-awesome}"))
 FontAwesome is Awesome 
>>> print(fa.format("{fa-font-awesome} {fa-does-not-exist}"))
 {fa-does-not-exist}
```
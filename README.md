# TODO.py
---

I was learning python, and coming from JS, I did the only thing I knew how to do. I made an (MVC) todo list app. It runs
entirely in the command line, is extremely basic, and it only has been tested on a mac. It currently only stores TODOs
in memory, so don't put anything too important in it. WIP.

---

# Running

If you want to run this, first you must create the [virtualenv][] (requires [virtualenv][]):

```bash
$ virtualenv venv
```

Then activate it (For convenience, a [`.env`][dotenv] is included, to do this automagically):

```bash
$ . ./venv/bin/activate
```

Then install the dependencies:

```bash
$ pip install -r requirements.txt
```

Then run it.

```bash
$ python main.py
```

---

# License

[MIT: ariporad.mit-license.org](http://ariporad.mit-license.org)


[virtualenv]: https://virtualenv.pypa.io/en/latest/
[dotenv]: https://github.com/kennethreitz/autoenv

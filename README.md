# Ulauncher Laravel Extension

Ulauncher extension for quick access to the Laravel documentation.

[![Become a Patron](https://img.shields.io/badge/Become%20a-Patron-f96854.svg?style=for-the-badge)](https://www.patreon.com/laravelista)

## Overview

Once you install this extension, just start Ulauncher and type: `l`. That will start the extension.

![Command](./screenshots/command.png)

From there you can type the slug of the documentation page you want to read like so: `l routing` and press Enter. That will open your browser to the routing page for the latest version of Laravel.

![Default Laravel Version](./screenshots/default.png)

If you want a specific Laravel version just type: `l 5.8/routing` and press Enter.

![Specific Laravel Version](./screenshots/specific.png)

## Installation

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```
https://github.com/mabasic/ulauncher-laravel
```

## Development

```
git clone git@github.com:mabasic/ulauncher-laravel.git
cd ulauncher-laravel
make attach
```

The `make attach` command will symlink the cloned repo into the appropriate location on the ulauncher extensions folder. _If the extensions folder does not exist, create it and run the command again._

Make sure Ulauncher is not running and from command line run:

```sh
ulauncher --no-extensions --dev -v |& grep "laravel"
```

This will start ulauncher with all the extensions disabled which will make it easier to look for logs.

You then have to start the Laravel extension manually. In the output of the previous command you should find something similar to this:

```sh
VERBOSE=1 ULAUNCHER_WS_API=ws://127.0.0.1:5054/ulauncher-laravel PYTHONPATH=/usr/lib/python3/dist-packages /usr/bin/python3 /home/mabasic/.cache/ulauncher_cache/extensions/ulauncher-laravel/main.py
```

Copy and run that command in another terminal window.

Your extension should now be running. To see your changes, just Ctrl+C and re-run the last command.
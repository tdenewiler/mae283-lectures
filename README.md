# MAE 283 Lectures

| Service | Status |
| ------- | ------ |
| Linters | [![Travis-CI](https://api.travis-ci.org/tdenewiler/mae283-lectures.svg?branch=master)](https://travis-ci.org/tdenewiler/mae283-lectures/branches) |

This repository contains lecture notes completed for [MAE 283](http://mechatronics.ucsd.edu/mae283a/) at UC San Diego
during Fall quarter 2009 and taught by Prof de Callafon.

You can compile using

```shell
pdflatex mae283_lectures.tex
bibtex mae283_lectures.aux
pdflatex mae283_lectures.tex
pdflatex mae283_lectures.tex
```

After running those commands initially, further changes can be compiled just running a single `pdflatex` command.

## Static Analysis

[Statick](https://github.com/sscpac/statick) is used to ensure consistent style and that certain classes of errors
do not exist in this repository.
To run Statick locally, do the following:

```shell
apt install chktex lacheck
pip install -r requirements.txt
mkdir statick_output
statick . statick_output --user-paths statick_config --profile tex-profile.yaml --config tex-config.yaml
```

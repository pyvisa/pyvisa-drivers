# pyvisa-drivers

A repository for community contributed instrument drivers using PyVISA

## What is it?

Quite simply, it is meant to be a collection of community contributed
instrument drivers with only these minimum requirements:

1. Written in Python and using PyVISA
2. Each driver is self contained

## Installation

Clone this repository, or just download the drivers you need directly
from the website.  Each driver (either module or package) is self
contained, so you can download the entire repository or download only
the drivers that you need.

## Why this, here and now?

A number of other projects already exist to provide a framework for
building high quality instrument drivers with a consistent interface,
such as LabPy, PyMeasure, Python-IVI and others.  The goals of this
repository are different.  If nothing else, it can serve as a
collection of community contributed examples demonstrating how to use
PyVISA.

Beyond that the hope is that by removing the requirements of any
particular convention, users will contribute what they have.  Many
python users will write their own driver for their own needs and
likely will only implement the subset of instrument control required
for their project.  PyVISA users are strongly encouraged to contribute
their code even if they feel it is incomplete.  The philosophy of this
repository is that a large collection of feature-incomplete drivers
has its place, with the hope that over time users will implement the
features they need and contribute what they have back to the
repository.

## How do I contribute a driver?

Fork this repository and submit a pull request.

Contributors are requested to put as much documentation in the code as
possible using docstrings and comments.

Remember that drivers should be self-contained, meaning provided as a
python module or a python package.  An organization of drivers by
vendor or instrument type has not been decided upon and probably won't
be set up until a critical mass of drivers has been established, so
for now, please put all self-contained drivers in the
pyvisa-drivers/drivers/ directory.

## Licensing

Drivers are by default distributed with the MIT license, the same as
for PyVISA.  If you wish to post a driver under a different license,
please include your driver as a separate package and include a license
file along with it.

## How do I get help?

To be determined. @dvincentwest will be assuming primary
responsibility for maintaining this repository but the drivers are
provided without warranty or support.  @dvincentwest will be screening
code to look for anything out of the ordinary, but given the goals of
this repository, support questions are likely to be similar to
low-level PyVISA usage questions.

I will explore options for discussion mailing lists, probably setting
something up in parallel to what PyVISA uses right now.

Driver Documention will be contained within the driver itself,
although at some point in the future a documentation page may be
established if the situation warrants it.

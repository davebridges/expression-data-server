'''The :mod:`~genes` app contains gene and transcript level data for expression data.

The goals of this package are:

* to generate a unique identifier for each expression object.
* to incorporate data from webservices to keep identifiers up to date.
* to maintain compatibility with future upgrades by maintaining expired gene and transcript names.

We have chosen to use the mouse ENSEMBL dataset as our list of canonical gene names and locations, but this can be over-ridden by changing the datasets file.
'''
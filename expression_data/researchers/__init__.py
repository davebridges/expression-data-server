'''The :mod:`researchers` app contains data on research personnel.

The :class:`~researchers.models.Researcher` model is a UserProfile model (see https://docs.djangoproject.com/en/dev/topics/auth/#storing-additional-information-about-users) and is generated automatically for every new :class:`~django.contrib.auth.models.Users`.

The goals of this app are:

* to attach :class:`~researchers.models.Researcher`  to :class:`~experiments.models.Experiment` objects.
* to provide the possibile restriction of data to specific users.
* to provide a user specific landing page (defined by **researcher-detail**).
'''

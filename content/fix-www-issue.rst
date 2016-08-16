DNS error when going to www subdomain of github pages hosted website
####################################################################

:date: 2016-08-15
:tags: meta, blog, help, dns, google, domain
:category: meta
:slug: dns-error-fix

.. image:: images\dns_error_small.png
    :alt: dns_unresolved_hostname


I was having an issue when trying to access my blog through the www subdomain, but I managed to fix it!
In an effort to help as many people as I can, I have decided to make a blog post every time I find an issue that I couldn't solve trivially through googling. 
I plan to create another blog post in the future that goes through exactly how I created this blog, but first let's see if I can't help someone.


My Stack
~~~~~~~~

Here is a list of relevant technologies I'm using to bring this blog to you: 

    - `Google Domains <https://domains.google.com>`_ $12/year for a domain managed by google
    - `Github Pages <https://pages.github.com/>`_ Free hosting with some very `reasonable limits <https://help.github.com/articles/what-is-github-pages/#recommended-limits>`_ (if I reach those limits I'll happily move to a paid host)

I had setup a github repo with a project page by creating a ``gh-pages`` branch, setting the custom domain, and creating a ``CNAME`` file with the following contents:

::

    superfluoussextant.com
    www.superfluoussextant.com


I had also setup the following custom resource records through google's DNS settings


.. figure:: images\dns_records.png
    :alt: Name: @, Type: A, Data: 192.30.252.153; 192.30.252.154. Name:www, Type: CNAME, Data: jchapman.github.io/superfluoussextant


My Issue
~~~~~~~~

Although I could reach my my blog through the apex domain ``superfluoussextant.com``, but not through the www subdomain ``www.superfluoussextant.com``. 
The error I saw was: ``dns_unresolved_hostname``, you can see how it expressed itself in the image below.


.. figure:: images\dns_error.png
    :alt: dns_unresolved_hostname

I had been following the excellent tutorial by Curtis Larson, which can be found `here <http://www.curtismlarson.com/blog/2015/04/12/github-pages-google-domains/>`_. 
There was a bit of a difference between his tutorial and what I wanted to do: he was using a custom domain for a user github page while I was trying to use a custom domain with a project page.
These difference between the two is the default url where they are served by github pages.
By default user pages are served at ``user.github.io`` while project pages are served at ``user.github.io/projectName``.

The Fix
~~~~~~~

Because I was publishing a project page, I strayed from the tutorial by setting my CNAME record to ``jchapman.github.io/superfluoussextant``, however this was not correct.
Even though I am trying to publish a project page instead of a user page, I still needed to make that CNAME record point to ``jchapman.github.io``.
The correct records are below, the changed one is highlighted.

.. figure:: images\dns_records_fixed.png
    :alt: Fixed dns record: Type: CNAME, Data: jchapman.github.io


If you're having a similar issue all you have to do is make sure that your CNAME record points to ``username.github.io`` even if you are trying to publish a project page with a custom domain. 
Also remember that it takes some time for DNS record changes, for me it was at least an hour.


Please let me know if this helped you by commenting below!

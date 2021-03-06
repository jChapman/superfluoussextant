How to set up blog with github pages and google domains
#######################################################

:date: 2016-08-16
:tags: meta, blog, help, domain
:category: meta
:slug: how-to-make-blog

My goals when creating this blog were

    1. To pay as little as possible
    2. Make it look good 
    3. Make it easy to write content.

Because of these goals I chose to use `google domains <http://domains.google.com>`_ and `Github Pages <https://pages.github.com/>`_ (also `Pelican <getpelican.com>`_ for content, but that's for another blog post).
To help get my blog up and running I used a `tutorial <http://www.curtismlarson.com/blog/2015/04/12/github-pages-google-domains/>`_ I found on `Curtis Lawson's Blog <http://www.curtismlarson.com/blog/>`_, however I noticing a couple differences I decided to write my own tutorial.

Step 1: Get a domain
--------------------

Go to http://domains.google.com and register a domain there. The .com domains are just $12 a year, plus it's through google.

Step 2: Create your Github repo
-------------------------------

    - Create a new repo on github, name it what ever you want.
    - Clone the new repo, create a branch named ``gh-pages`` and add a simple index.html file to that newly created branch.
    - Push up the new branch

Here's what I typed to accomplish those steps (will probably be different for you)

.. code:: bash

    git clone https://github.com/jChapman/testBlog.git
    cd testBlog
    git checkout -b gh-pages
    echo testing > index.html
    git add index.html
    git commit -m "Added simple index page"
    git push --set-upstream origin gh-pages


We can then test that our page is being served by Github Pages by going to the settings page of the repo on on Github.com.
If we scroll down to the Github Pages section you should the following:

.. figure:: images/first_success.png
    :alt: Your site is published at https://jchpaman.github.io/testBlog


Step 3: Setting up your repo for a custom domain
------------------------------------------------

Next we want to use the domain we purchased instead of the github.io url.
First a file named ``CNAME`` to your ``gh-pages`` branch. The ``CNAME`` file should only contain a single line either ``yoursitename.com`` or ``www.yoursitename.com`` depending on how you want to site to be presented.
There are `some people <http://no-www.org/>`_ who have `strong opinions <http://www.yes-www.org/>`_ about this, I am not one of them.
Here is how I added that file in bash:

.. code:: bash

    echo superfluoussextant.com > CNAME
    git add .
    git commit -m "Adding custom domain"
    git push

You can confirm that you did this correctly by going to the settings page of the repo on Github.com.
If you scroll down to the Github Pages section, you should see something like the following

.. figure:: images/second_success.png
    :alt: Your site is ready to be published at https://superfluoussextant.com


Step 4: DNS settings for your domain
------------------------------------

Finally we need to change the DNS setting for our domain to point to the Github server hosting our content.
Go to `domains.google.com <domains.google.com>`_ and click on "Configure DNS" next to your domain name.
Now scroll down to Custom resource records, add the following records:

    - Name: @, Type: A, Data: 192.30.252.153; 192.30.252.154
    - Name: www, Type: CNAME, Data: username.github.io

.. figure:: images/third_success.png
    :alt: Just read above

    You records should look something like this


The first record is an Alias record which points your domain at the specified ip addresses, in this case we use the Github Pages addresses of ``192.30.252.153`` and ``192.30.252.154``.
The ``@`` simply refers to your whole domain.

The second record is a canonical name record which maps alias names to a canonical name. We want to map to our Github pages url.


.. note:: Like I said in my `previous blog post <http://superfluoussextant.com/dns-error-fix.html>`_ even though this is a project page and is hosted at ``yourname.github.io/projectName``, make sure that your CNAME record points to ``yourname.github.io``.
.. note:: It make take some times for the DNS settings to be applied. It has taken me at least an hour, but give it at least 3 until you give up and start blaming yourself.

After waiting an appropriate amount of time, test your website by going to your custom domain and see if your content is served.


How to Make Gifs Using Python
#############################

:date: 2017-04-16
:tags: programming, python, imagemagick, gif, jif, animation
:category: programming
:slug: making-gifs-with-python

Intro
=====

While gifs are an outdated format and terribly inefficient, they remain a popular way to communicate on the internet. 
With so many ways to create, modify, and inspect images (`Pillow <https://pillow.readthedocs.io/en/latest/>`_, `OpenCV <http://opencv.org/>`_, and even `scipy <http://www.scipy-lectures.org/advanced/image_processing/>`_)
in Python it seems only natural to want to make gifs in the same environment in which you created or edited your image.
Like many tasks you want to accomplish in Python, someone has already done it and there are libraries to assist you. 
Also like many other tasks you want to accomplish in Python there are several different packages that can be used to create gifs.


The Setup
---------
I will present a couple options and show you how to use each of them to generate a gif from a series of still pictures.
This is my common use case, I have a series of images which represent some changing system and I want to animate the change.


For example here is a series of images I made:

.. image:: images/gifThis.png
    :alt: A bunch of similar images


... and here is a generated gif:

.. image:: images/gifThis.gif
    :alt: An animated gif

Some assumptions

* Python 3
* You are in the directory with the images you want to turn into a gif
* All the images are named so that lined up numerically they are in the order they should be shown in the gif (in the above image ``brains_40.png`` comes first then ``brainz_50.png`` and so on until ``brainz_183.png`` which will be the last frame)



Option 1: ImageMagick
=====================

Love it or hate it `ImageMagick <https://www.imagemagick.org/>`_ has been around for a long time and is available for the three major operating systems (Linux, OSX, and Windows) and is even available in many Linux package repositories.
For this reason my go to when first trying to make a gif was ImageMagick by simply calling it through `subprocess <https://docs.python.org/3/library/subprocess.html>`_. The implementation is below 

.. code:: python

    import glob
    import os

    gif_name = 'outputName'
    file_list = glob.glob('*.png') # Get all the pngs in the current directory
    list.sort(file_list, key=lambda x: int(x.split('_')[1].split('.png')[0])) # Sort the images by #, this may need to be tweaked for your use case

    with open('image_list.txt', 'w') as file:
        for item in file_list:
            file.write("%s\n" % item)

    os.system('convert @image_list.txt {}.gif'.format(gif_name)) # On windows convert is 'magick'

Why can't we just run `convert *.png out.gif`? Because this sorts the images alphabetically which puts 10 before 2.

Why do you have to write a file out instead of just listing the individual files in the command? Command length restraints, if you have 100 images each names blah_# then that is at least 600 characters.

While this works and since I already had ImageMagick installed it was easy enough to implement, but it doesn't feel pythonic since we have to call an external program so let's look at more python-y solutions.


Option 2: MoviePy
=================

.. https://github.com/avyfain/conway/blob/master/conway/images.py
.. https://zulko.github.io/blog/2014/09/20/vector-animations-with-python/

I discovered `MoviePy <https://zulko.github.io/moviepy/index.html>`_ while looking to solve this problem and it looks very promising. 
While it looks like it's primarily designed to make or edit videos it has gif making capability.
What's more it can even use ImageMagick as a `back end for image conversion <https://zulko.github.io/moviepy/install.html#other-optional-but-useful-dependencies>`_ (otherwise it uses `imageio <https://imageio.readthedocs.io/>`_).

.. code:: python

    import glob
    import moviepy.editor as mpy

    gif_name = 'outputName'
    fps = 12
    file_list = glob.glob('*.png') # Get all the pngs in the current directory
    list.sort(file_list, key=lambda x: int(x.split('_')[1].split('.png')[0])) # Sort the images by #, this may need to be tweaked for your use case
    clip = mpy.ImageSequenceClip(file_list, fps=fps)
    clip.write_gif('{}.gif'.format(gif_name), fps=fps)

I have found that it `fails to make gifs out of greyscale images <https://github.com/Zulko/moviepy/issues/190>`_ (the example I gave above was using greyscale images).
Other than that one issue MoviePy seems very nice, even printing out the backend used and a progress bar when creating the gif.

.. image:: images/moviepyoutput.png
    :alt: [MoviePy] Building file outputName.gif with imageio 100%|##########| 51/51 [00:00<00:00, 53.29it/s]

The creator of MoviePy has some interesting examples of using it to create gifs for example `Vector Animations With Python <https://zulko.github.io/blog/2014/09/20/vector-animations-with-python/>`_ and `Data Animations With Python and MoviePy <https://zulko.github.io/blog/2014/11/29/data-animations-with-python-and-moviepy/>`_ .

Other Options
=============

Here are some other options I looked into, but didn't use for various reasons.

Pillow
------

.. https://stackoverflow.com/questions/24688802/saving-an-animated-gif-in-pillow

I use `Pillow to generate images <https://pillow.readthedocs.io>`_ , it would be great to use it to generate the gifs. 
It even appears that gifs are one of the `"fully supported formats" <https://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html>`_ !
I even had hope that I could progressively save frames as they were created with the `append_images` `argument <https://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html#saving>`_ .
However the more I looked into creating gifs with Pillow the more `bugs I found <https://github.com/python-pillow/Pillow/issues?utf8=%E2%9C%93&q=is%3Aissue%20is%3Aopen%20gif>`_ including the fact that simply re-saving a gif increases the size of the gif.

For now I'm going to stick to one of the other options listed above because of the known (and unknown) issues in Pillow.

Here's an example of using Pillow to make gifs: https://github.com/JuanPotato/Legofy/blob/master/legofy/images2gif_py3.py

Wand
----

`Wand <http://docs.wand-py.org/>`_ is a Python wrapper for ImageMagick, which sounds great for anyone used to ImageMagick (aka convert). However it is `not compatible <https://github.com/dahlia/wand/issues/316>`_ with the latest version of ImageMagick and does not appear to be actively maintained. 

(Maybe there is something to be said for reasons that `GraphicsMagick split from ImageMagick <http://www.graphicsmagick.org/FAQ.html#how-does-graphicsmagick-differ-from-imagemagick>`_)



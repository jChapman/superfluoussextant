Generative Art Setup
####################

:date: 2017-04-24
:tags: programming, art, python, PIL, Pillow
:category: programming
:slug: generative-art-intro
:header_cover: /images/rootedMoonInverse.png

What is generative art?
=======================

In general `generative art <https://en.wikipedia.org/wiki/Generative_art>`_ is defined as art that has been (at least in some part) created by using an autonomous system.
I think of it as art that is created by some system, but the artist (not the system although some may argue that the system is the true artist) doesn't know exactly how it will turn out.
While the artist can tweak some parts of the system (usually the inputs) they do not have full control of the generation of the artwork.

I recently discovered generative art after reading an excellent article by Anders Hoff, titled `On Generative Algorithms <http://inconvergent.net/generative>`_. 
I found it to be a very interesting read, well worth your time, and it inspired me to make my own generative algorithms. 
In particular the `first example, Hyphae <http://inconvergent.net/generative/hyphae/>`_, interested me. 
I thought, hey I bet I can do that in a couple lines of python!

After playing around with a couple of examples I extracted a basic framework for creating generative art that I thought was worth sharing.

The Tools of the Trade
======================

Python, for prototyping it's hard to beat python in terms of speed of development/iteration and available libraries.

Pillow, PIL was Python Image Library until it stopped getting updated. Pillow is a fork of PIL that is actively maintained. Pillow allows us to quickly create, edit, and save images.

MoviePy, as mentioned in a `previous post <{filename}pygif.rst>`_ is a great way to generate GIFs from a series of still images. I use it to (guess what) generate gifs from still images.

Using the Tools
===============

Here's an outline of the steps that my Python script does for each invocation

#. Create a new directory relative to this script, call it the current date so that the name won't conflict and the directory are in a sane order
#. Copy the current version of this script to the newly created directory, this allows me to jump back to a previous state if I liked the results or if my more recent changes were too drastic or if the output of a previous version was particularly interesting.
#. Do the work, for each frame/step draw on a Pillow Image.
#. Save the current image, make the name something that will allow for some kind of order such as appending the current itteration to the file name such as appending the current iteration to the file name.
#. Create the GIF using MoviePy.

The Script
==========

.. code:: python

    import os
    import shutil

    from datetime import datetime
    from PIL import Image

    # Get the current time, use it as the directory we save everything in
    SAVE_DIR = datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    os.mkdir(SAVE_DIR)
    shutil.copy(__file__, SAVE_DIR)  # Save a copy of this script so that we can recreate stuff

    # The size of the image
    IMAGE_SIZE = 100, 100
    # Create a new image
    CURRENT_IMAGE = Image.new('RGB', IMAGE_SIZE)

    # Missing: initial setup

    # How many iterations?
    MAX_ITERATIONS = 100
    # The main loop, mess with the image for each iteration
    for i in range(MAX_ITERATIONS):
        # Manipulate the image before saving it
        CURRENT_IMAGE.save(os.path.join(SAVE_DIR, "{}.png".format(i)))

        # Every so often print out something so we get a sense of progress
        if i % 10 == 0:
            print('Iteration {}'.format(i), flush=True)


    def gifit(image_loc, gif_name, fps=12):
        """ Creates a GIF from all the pngs in the provide image_loc """
        import glob
        import moviepy.editor as mpy

        os.chdir(image_loc)
        file_list = glob.glob('*.png')
        list.sort(file_list, key=lambda x: int(x.split('.png')[0]))
        clip = mpy.ImageSequenceClip(file_list, fps=fps)
        clip.write_gif('{}.gif'.format(gif_name), fps=fps)


    gifit(SAVE_DIR, 'final')

Example
=======

Here's an example using the basic script from above. We first place randomly
colored pixels then for each iteration we select pixels in random order and 
have them "fight" against an adjacent pixel. The winning pixel transfers their
color to the losing pixel. In this first example we chose the pixel whose red 
value is larger as the winner.

.. code:: python

    import os
    import random
    import shutil

    from datetime import datetime
    from PIL import Image

    # Get the current time, use it as the directory we save everything in
    SAVE_DIR = datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    os.mkdir(SAVE_DIR)
    shutil.copy(__file__, SAVE_DIR)  # Save a copy of this script so that we can recreate stuff

    # The size of the image
    IMAGE_SIZE = 100, 100
    # Create a new image
    CURRENT_IMAGE = Image.new('RGB', IMAGE_SIZE)
    PIXELS = CURRENT_IMAGE.load()  # Get a modifiable representation of the image

    # Initial setup, make each pixel a random color
    for x in range(0, IMAGE_SIZE[0]):
        for y in range(0, IMAGE_SIZE[1]):
            PIXELS[x, y] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


    def get_random_adjacent(loc):
        """ Gets a random adjacent pixel that is not out of bounds"""
        _x = loc[0]
        _y = loc[1]
        adjacent_x, adjacent_y = [(_x, _y+1), (_x, _y-1), (_x+1, _y), (_x-1, _y)][random.randint(0, 3)]
        if adjacent_x < 0:
            adjacent_x = IMAGE_SIZE[0]-1
        elif adjacent_x > IMAGE_SIZE[0]-1:
            adjacent_x = 0
        if adjacent_y < 0:
            adjacent_y = IMAGE_SIZE[1]-1
        elif adjacent_y > IMAGE_SIZE[1]-1:
            adjacent_y = 0
        return (adjacent_x, adjacent_y)


    def determine_winner(one_pixel, another_pixel):
        """Pick a winning color given two colors"""
        if one_pixel[0] > another_pixel[0]:
            return one_pixel
        return another_pixel


    # How many iterations?
    MAX_ITERATIONS = 100
    # The main loop, mess with the image for each iteration
    for i in range(MAX_ITERATIONS):
        for x in random.sample(range(CURRENT_IMAGE.size[0]), k=CURRENT_IMAGE.size[0]):
            for y in random.sample(range(CURRENT_IMAGE.size[1]), k=CURRENT_IMAGE.size[1]):
                location = (x, y)
                opponent_location = get_random_adjacent(location)

                winner = determine_winner(PIXELS[location], PIXELS[opponent_location])

                # Update pixels
                PIXELS[location] = winner
                PIXELS[opponent_location] = winner

        CURRENT_IMAGE.save(os.path.join(SAVE_DIR, "{}.png".format(i)))

        # Every so often print out something so we get a sense of progress
        if i % 10 == 0:
            print('Iteration {}'.format(i), flush=True)

    ...

    gifit(SAVE_DIR, 'final')

Here is the result of this script:

.. image:: images\red_fight.gif
    :alt: Fighting pixels

You might first expect that the system would become a single large red square,
however it resolves into some red, some pink, and even some yellow pixels. This
is because each of them have the same value for red and towards the end the
winner is simply whoever was the first chosen pixel.

The beauty of our setup is that we can quickly change a couple lines and create
a completely different system. Let's modify the `determine_winner` function so
that only the truly "red-ist" pixel wins.

.. code:: python

    def determine_winner(one_pixel, another_pixel):
        """Pick a winning color given two colors"""
        one_sum = one_pixel[0] - one_pixel[1] - one_pixel[2]
        other_sum = another_pixel[0] - another_pixel[1] - another_pixel[2]
        if one_sum > other_sum:
            return one_pixel
        return another_pixel

... and here's the result, the other colors quickly disappear and it becomes a fight to the true red (255, 0, 0)

.. image:: images\super_red.gif
    :alt: Fighting pixels, spoiler: red wins


Finally for your enjoyment here's a large version of the previous red fighting

.. image:: images\big_red.gif
    :alt: Fighting pixels, spoiler: red wins

Bonus
=====

Some suggested additions 

Don't clobber pixels
--------------------

If a pixel has already "fought" this iteration don't make it "fight" again

To do this, just keep a map of all those that have fought

.. code:: python

    for i in range(MAX_ITERATIONS):
        fought = {}
        for x in random.sample(range(CURRENT_IMAGE.size[0]), k=CURRENT_IMAGE.size[0]):
            for y in random.sample(range(CURRENT_IMAGE.size[1]), k=CURRENT_IMAGE.size[1]):
                location = (x, y)
                opponent_location = get_random_adjacent(location)
                if location in fought:
                    continue
                if opponent_location in fought:
                    continue

                winner = determine_winner(PIXELS[location], PIXELS[opponent_location])

                # Update pixels
                PIXELS[location] = winner
                PIXELS[opponent_location] = winner

                # Update fought map
                fought[location] = True
                fought[opponent_location] = True

        CURRENT_IMAGE.save(os.path.join(SAVE_DIR, "{}.png".format(i)))

        # Every so often print out something so we get a sense of progress
        if i % 10 == 0:
            print('Iteration {}'.format(i), flush=True)


Open the gif
------------

After running the script it's nice to see the generated gif to get immediate feedback.

To do this I would simply run a command at the bottom of the script that opened an application that can handle gifs 

.. code:: python

    import subprocess

    # Or chrome or okular or ...
    subprocess.run('preview final.gif')

    # Or, in Windows
    subprocess.run('start final.gif', shell=True)


Final Thoughts
==============

Have fun and mess around with this script. I've found this setup very conducive
to quick iteration and experimentation that can quickly produce some very
interesting results. If you made anything similar I would love to see it, I
find these kinds of animated images very interesting and relaxing.

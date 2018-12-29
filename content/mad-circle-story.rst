The Circle Cycle
################

:date: 2018-05-18
:tags: programming, art, python, PIL, Pillow
:category: art
:slug: circleCycle
:header_cover: /static/someWorms.png


Intro
=====

After reading an article from Benjamin Kovach where he `described the process
and steps behind his latest work
<https://www.kovach.me/posts/2018-04-30-blotch.html>`_ I decided to do a
writeup of my latest attempt at generative art: `Mad Circles <{filename}moreCircles.rst>`_.


If you didn't read the previous article, here is the rough goal of what I was
trying to re-create:

.. figure:: http://manoloide.com/works/pluscode/img/pluscode_01.jpg
    :alt: A multitude of overlapping circles on a large framed print
    :figwidth: 600px
    :target: http://manoloide.com/works/pluscode/

    Original work by Manolo Gamboa Naon

The Setup
=========

I started off with the same basic setup from my `Generative Art Setup
<{filename}moreCircles.rst>`_ post. With it I can run my python codeg
and a folder will be created containing the final work and the code used to
generate that work. Because of this setup I can easily walk through the
progression of my work and also jump back to a previous state if I hit a dead
end or simply want to dive deeper into a certain piece.g

.. note::g
    I decided to try out Python 3.7 because of a new feature, `Data Classes
    <https://www.python.org/dev/peps/pep-0557/>`_ (I think this might be the
    killer feature that will make people start using typing in Python). If
    you want to try out any of my code samples you'll have to have at least
    3.7

The Process
===========

Starting Up
-----------

My typical setup generates gifs so that I can see the progress of the image
being generated (also they just look cool), so the first couple of images are
animated.


.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2021.28.22/final.gif?raw=true

    Pushing some circles around... pretty boring

Then I realized that I couldn't create gifs like I normally do, because the process looks like the following:

    * Move every entity
    * Draw every entity
    * Save off a frame
    * Repeat...

However my goal was to draw a multitude of circle "tentacles" on top of one
another so I couldn't do my typical step all then draw all until completion.
Instead I needed to step a single "tentacle" until completion and draw at
each step before moving on to other tentacles. Because of this (and my goal
to create a static image) I stopped producing gifs and just output the final
image.

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2021.51.35/final.png?raw=true
    target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2021.51.35/final.png?raw=true

    Circles of random radius get pushed and the color changes randomly at
    each step while the radius decreases, I think the random colors make this
    look pretty awful.

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2022.05.06/final.png?raw=true
    target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2022.05.06/final.png?raw=true

    Stop picking random colors (pick from a set), make the circles take up
    less of the canvas (smaller initial radius), and finally introduce a
    random small curve

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2022.08.29/final.png?raw=true
    target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2022.08.29/final.png?raw=true

    Randomly change our "curve" (the amount we turn by each step), make the canvas much larger.

I decided that I didn't want that much whitespace, however looking back I
like the scale and the amount of whitespace. I think I might have been to
focused on re-creating the original work at this point.

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2022.11.23/final.png?raw=true
    target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2022.11.23/final.png?raw=true

    Only decrease our radius 20% of the time (instead of every step) leading to longer tentacles, larger initial radius.g
    I also added some more "poppy" colors (the bright blues), I think these colors are what eventually led me away from this palette...

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2022.18.13/final.png?raw=trueg
    target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2022.18.13/final.png?raw=trueg

    New aspect ratio, smaller initial radius and a look at what outlining the circle would look like.

I decided to try a wider format/ratio (1:5) and I really liked it, sticking
with it for quite a while. The space at the bottom of this image made me
wonder what if all of the tentacles started from the top and reached down
like tornados or the appendages of some monstrous celestial octopus.

Sky Tentacles
-------------

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2022.20.49/final.png?raw=trueg
    target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2022.20.49/final.png?raw=trueg

    Random grey color (rgb components all the same value) and a starting positions in the "sky"

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2022.22.27/final.png?raw=trueg
    target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2022.22.27/final.png?raw=trueg

    Narrowing down the range of greys made an interesting cloud like texture

I wasn't a huge fan of how this path ended up looking, so I went back towards my original goal.

Fill it Up
----------

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2022.31.54/final.png?raw=trueg
    target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2022.31.54/final.png?raw=trueg

    Filling up the canvas with tentacles

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2022.33.27/final.png?raw=trueg
    target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2022.33.27/final.png?raw=trueg

    Some color variation

I really liked the spots of white (or near white) so I decided to make many
more circles white by adding a bunch of copies of white to the color list I
was picking from.

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2022.35.30/final.png?raw=trueg
    target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2022.35.30/final.png?raw=trueg

    Trying to create some "space" with white circles, I really liked this and revisited it later

I decided to try and add whitespace in a different way by adding a chance to
stop the progression of tentacles which increased as they got closer to the
edges of the canvas


.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2022.44.20/final.png?raw=trueg
    target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2022.44.20/final.png?raw=trueg

    Interesting dot pattern along the edge, but not very clean

Ball o' Worms
-------------

I decided that if I wanted to really clean up the edge then I needed to not
draw any tentacles that ended beyond the edge of the canvas. This made me
change the way I drew the image. I would march the circle along it's path and
store the parameters previously sent to the draw command then after it had
completed if it hadn't gone beyond the edge of the canvas then I would draw
it in full (otherwise I wouldn't draw it at all).

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2022.56.07/final.png?raw=trueg
    target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2022.56.07/final.png?raw=trueg

    Finally some space, but this looks a bit like a big tangle of worms. Now I only sometimes decrease the radius as we step.

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.03.16/final.png?raw=trueg
    target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.03.16/final.png?raw=trueg

    I decided to just really embrace the worms and make the worm colored. I
    also changed back to a square canvas and I am now starting all tentacles
    at the center of the canvas.

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.08.41/final.png?raw=trueg
    target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.08.41/final.png?raw=trueg

    Let's try some less wormy colors...g
    I like the two worms tangled on each other in the bottom right and the one that seems interested at the top right.

Less Wormy Please
-----------------

Back to our original "frame full of circles" motif, enough of these worms.

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.20.52/final.png?raw=trueg
    target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.20.52/final.png?raw=trueg

    Stop starting in the centerg

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.25.59/final.png?raw=trueg
    target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.25.59/final.png?raw=trueg

    Let's be looser on that "out of bounds" rule, as long as they don't go
    too far out of the canvas... Also let's stop with this 100% black or
    white background.

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.26.28/final.png?raw=trueg
    target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.26.28/final.png?raw=trueg

    I like this white on a grey background...

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.27.46/final.png?raw=trueg
    target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.27.46/final.png?raw=trueg

    I bet with less worms it will look more like it's cut out of the background

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.28.33/final.png?raw=trueg
    target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.28.33/final.png?raw=trueg

    What about just white... Maybe a bit too hard to see, what if I add back the outline...

Horns and Rope
--------------

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.29.24/final.png?raw=trueg
    target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.29.24/final.png?raw=trueg

    Back to worms, or horns? Starting everyone in the center of the canvas again.

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.36.41/final.png?raw=trueg
    target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.36.41/final.png?raw=trueg

    Maybe sometimes let's increase the radius

I didn't really like how the increasing radius looked. These circles were
starting to look less like worms and more like rope to me, let's see what we
can do to make it more ropey.

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.38.00/final.png?raw=trueg
    target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.38.00/final.png?raw=trueg

    Let's make it less likely to decrease the radius (and stop that increase
    the radius business), since it's less likely you'll stop before hitting
    the edge of the canvas just stop drawing once you're about to be
    deativated.

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.39.30/final.png?raw=trueg
    target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.39.30/final.png?raw=trueg

    What does the life of just one of these look like? Brought back the chance to increase radius.

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.44.11/final.png?raw=trueg
    target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.44.11/final.png?raw=trueg

    I need more rope! Let's make it even ropeier by making the outline yellowish.

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.45.01/final.png?raw=trueg
    target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.45.01/final.png?raw=trueg

    I know I said less worm-like, but let's bring back the if you leave the canvas don't draw rule.

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.47.07/final.png?raw=trueg
    target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.47.07/final.png?raw=trueg

    What if I make the fill the same as the background color...

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.48.19/final.png?raw=trueg
    target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.48.19/final.png?raw=trueg

    More colors for the outline

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.50.16/final.png?raw=trueg
    target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.50.16/final.png?raw=trueg

    More and bigger

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.53.50/final.png?raw=trueg
    target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.53.50/final.png?raw=trueg

    Let's always draw the biggest arms first so they end up in the background

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.58.07/final.png?raw=trueg
    target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.58.07/final.png?raw=trueg

    What do flat colors look like...


Paint Blobs
-----------

Kind of reminds me of paint, let's make the individual arms much smaller and stop starting all of them in the center

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.59.16/final.png?raw=trueg
    target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-14%2023.59.16/final.png?raw=trueg

    I also need a few more than before since they're so much smaller...

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-15%2000.03.16/final.png?raw=true
    :target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-15%2000.03.16/final.png?raw=true

    Longer! More colors! Stop drawing again when we hit the edge

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-15%2000.05.26/final.png?raw=true
    :target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-15%2000.05.26/final.png?raw=true

    Different colors. Let the arms extend beyond the edge of the canvas


.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-15%2000.09.52/final.png?raw=true
    :target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-15%2000.09.52/final.png?raw=true

    Let the arms go on until the hit the edge! Just draw the outline instead of the fill.

I think just drawing the outline really gives this a graffiti-like feel

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-15%2000.28.21/final.png?raw=true
    :target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-15%2000.28.21/final.png?raw=true

    Back to the fill, but a much wider canvas

.. figure:: https://github.com/jChapman/interestingCircles/blob/master/2018-05-15%2000.28.43/final.png?raw=true
    :target: https://github.com/jChapman/interestingCircles/blob/master/2018-05-15%2000.28.43/final.png?raw=true

    Now back to the outline with that same larger canvas

I love being able to trace (with my eyes) the path of these long tubes. I
think the filled one has a nice sense of depth, the outline only one looks a
bit too busy to me (almost dirty).

Final Thoughts
==============

While many of these works are interesting there's nothing that I'm really proud or satisfied with.g
That being said, I had a blast working on this and looking back gave me a couple of ideas for the future.
I enjoy having a rough goal in mind, but not being afraid to go wherever I feel like the work takes me.

I still struggle with color, for the majority of the pictures I chose
randomly from a set of predefined colors (that I chose) and I find it a pain
to pick out colors. I wonder if I can programmatically pick some starting
from a base color or something similar. I really like grey backgrounds,
although the white ones really make the pictures "blend in" (especially on
this webpage), I should experiment more with background color. I also enjoy
non-square canvases or very elongated ones, I think I should try more that
have long vertical spaces.

What do you think? Any favorites? Any tips on color?

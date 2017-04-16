Logo Design Review
##################

:date: 2016-10-15
:tags: logo, creative, inkscape, graphic design, robot framework
:category: creative
:slug: robot-logo2

I'm Bad At Completing Things
============================

In general `generative art <https://en.wikipedia.org/wiki/Generative_art>`_ is defined as art that has been (at least in some part) created by using an autonomous system.
I think of it as art that is created by some system, but the artist (not the system although some may argue that the system is the true artist) doesn't know exactly how it will turn out.
While the artist can tweak some parts of the system (usually the inputs) they do not have full control of the generation of the artwork.

I recently discovered generative art after reading an excellent article by Anders Hoff, titled `On Generative Algorithms <http://inconvergent.net/generative>`_. 
I found it to be a very interesting read, well worth your time, and it inspired me to make my own generative algorithms. 
In particular the `first example, Hyphae <http://inconvergent.net/generative/hyphae/>`_, interested me. 
I thought, hey I bet I can do that in a couple lines of python!

Enter Circlepusher
==================

The goal is to push some circles around on a canvas that don't intersect with each other and randomly split into smaller circles to be pushed.
Let's start by making those circles, we need something to store a location, a radius, and some random angle

.. code:: python

    import random


    class Circle:
        def __init__(self, radius, location):
            """
            :param radius: radius of circle in pixels
            :param location: two tuple of x,y
            """
            self.radius = radius
            self.location = location
            self.angle = random.randint(0, 360)

        @property
        def x(self):
            return self.location[0]

        @property
        def y(self):
            return self.location[1]

What good's a circle if you can't see it (and is it even really a circle at all)? 
There's probably other ways to draw circles, but I'm going to use PIL(low) because it was pretty simple.
Also I'm going to use some globals because I don't care if this code is pretty, I want it to be easy to hack.


.. code:: python

    import random

    from PIL import Image, ImageDraw

    image = Image.new('L', (500, 500), 'white')
    image_draw = ImageDraw.Draw(image)


    class Circle:
        def __init__(self, radius, location):
            """
            :param radius: radius of circle in pixels
            :param location: two tuple of x,y
            """
            self.radius = radius
            self.location = location
            self.angle = random.randint(0, 360)

        def draw(self):
            image_draw.ellipse((self.x - self.radius,
                                self.y - self.radius,
                                self.x + self.radius,
                                self.y + self.radius), fill='black')

    circle = Circle(10, (250, 250))
    circle.draw()
    image.show()

Now we have a nice big black circle in the middle of our canvas, here's some docs on `PIL.Image.new <https://pillow.readthedocs.io/en/latest/reference/Image.html#PIL.Image.new>`_ (the L we specify tells Pillow that this will be a grayscale image, see `PIL Modes <https://pillow.readthedocs.io/en/latest/handbook/concepts.html#concept-modes>`_ if you want to learn more).

Now it's time to push it (push it real good)!

.. code:: python

    import random

    from PIL import Image, ImageDraw
    ...

    Class Circle:

    ...

        def push(self):
            # Let's step by 1/4 of the radius each time
            step = self.radius / 4
            rad_angle = math.radians(self.angle)
            self.location = (self.x + step*math.cos(rad_angle),
                             self.y + step*math.sin(rad_angle))

    circle = Circle(10, (250, 250))
    for _ in range(100):
        circle.draw()
        circle.push()
    image.show()


.. image:: /images/genline.png
    :alt: Just a single line starting at the center of a white square and continuing out to the edge

Woo! We have a single clock hand, not too impressive huh? 
However if we continue to increase the number of iterations we'll soon run off the edge of the canvas, let's prevent that by adding a check to the push function

.. code:: python

    import random

    import math
    from PIL import Image, ImageDraw

    image_bounds = (500, 500)
    image = Image.new('L', image_bounds, 'white')
    image_draw = ImageDraw.Draw(image)


    class Circle:
        def __init__(self, radius, location):
            """
            :param radius: radius of circle in pixels
            :param location: two tuple of x,y
            """
            self.radius = radius
            self.location = location
            self.angle = random.randint(0, 360)

        def draw(self):
            image_draw.ellipse((self.x - self.radius,
                                self.y - self.radius,
                                self.x + self.radius,
                                self.y + self.radius), fill='black')

        def push(self):
            # Let's step by 1/4 of the radius each time
            step = self.radius / 4
            rad_angle = math.radians(self.angle)
            next_step = (self.x + step*math.cos(rad_angle),
                         self.y + step*math.sin(rad_angle))
            if self.within_bounds(next_step):
                self.location = next_step

        @staticmethod
        def within_bounds(location):
            if location[0] < 0 or location[0] > image_bounds[0] or location[1] < 0 or location[1] > image_bounds[1]:
                return False
            return True
    ...

This doesn't take into account the radius of the circle being pushed, it only checks it's center.
Why should we `limit <http://www.catb.org/jargon/html/Z/Zero-One-Infinity-Rule.html>`_  ourselves to 2 circles?
Let's make 10!

.. code:: python

    for _ in range(10):
        circle = Circle(10, (250, 250))
        for __ in range(100):
            circle.draw()
            circle.push()

.. image:: /images/clockhands.png
    :alt: Just a bunch of lines starting in the center

Well... it is a thing, but not a very good thing. Let's make it so that they don't step on each other.
I'll start by adding the concept of deactivating a circle, if it bumps into another circle, let's not keep trying to push it.
Note that the method of detecting "collision" is pretty "stupid" since I'm just checking a single pixel ahead of us, we could still collide at any of the other pixels we're about to paint.
Next let's make sure we don't step over the edge of the canvas.
Finally let's add a little spin to the movement of our circles, a curve which will be added to the angle at each step.

.. code:: python

    import random

    import math
    from PIL import Image, ImageDraw

    image_bounds = (500, 500)
    image = Image.new('L', image_bounds, 'white')
    image_draw = ImageDraw.Draw(image)


    class Circle:
        def __init__(self, radius, location):
            """
            :param radius: radius of circle in pixels
            :param location: two tuple of x,y
            """
            self.radius = radius
            self.location = location
            self.angle = random.randint(0, 360)
            self.curve = random.randint(-45, 45)/100
            self.active = True

        @property
        def x(self):
            return self.location[0]

        @property
        def y(self):
            return self.location[1]

        def draw(self):
            if not self.active:
                return
            image_draw.ellipse((self.x - self.radius,
                                self.y - self.radius,
                                self.x + self.radius,
                                self.y + self.radius), fill='black')

        def push(self):
            if not self.active:
                return
            # Let's step by 1/4 of the radius each time
            step = self.radius / 4
            rad_angle = math.radians(self.angle)
            next_step = (self.x + step*math.cos(rad_angle),
                         self.y + step*math.sin(rad_angle))
            # Stepping by 1/4 of the radius will put us still inside our current radius, so let's look a bit further ahead
            big_step = (self.x + self.radius*2*math.cos(rad_angle),
                        self.y + self.radius*2*math.sin(rad_angle))
            if self.within_bounds(next_step) and self.free_spot(big_step):
                self.location = next_step
            else:
                self.active = False
                if self in circles:
                    circles.remove(self)

            self.angle = (self.angle + self.curve) % 360

        @staticmethod
        def within_bounds(location):
            if location[0] < 0 or location[0] > image_bounds[0] or location[1] < 0 or location[1] > image_bounds[1]:
                return False
            return True

        def free_spot(self, spot):
            # Simply check the canvas to see if the passed spot is white
            return self.within_bounds(spot) and image.getpixel(spot) == 255

    for _ in range(10):
        circle = Circle(10, (250, 250))
        for __ in range(1000):
            circle.draw()
            circle.push()
    image.show()

Now we have lines that curve beautifully, don't intersect with each other and stop without going over the edge of the canvas.
Finally we have something worth tinkering with.

.. image:: /images/curvylines.png
    :alt: Some fantastically curvy lines

Making Babies
=============
Time to mutate! Let's create some smaller versions of our tentacles that randomly come off of our main "branches".
Babies should probably be smaller then their parent(s?) so let's make their radius 75% of their parent.
While we're at it let's randomize the starting location of our circles.


.. code:: python

    import random

    import math
    from PIL import Image, ImageDraw

    image_bounds = (500, 500)
    image = Image.new('L', image_bounds, 'white')
    image_draw = ImageDraw.Draw(image)
    circles = []

    ...

    class Circle:

            ...
        def push(self):
            if not self.active:
                return

            if self.should_make_baby():
                circles.append(self.make_baby())

            # Let's step by 1/4 of the radius each time
            step = self.radius / 4
            rad_angle = math.radians(self.angle)
            next_step = (self.x + step*math.cos(rad_angle),
                         self.y + step*math.sin(rad_angle))
            # Stepping by 1/4 of the radius will put us still inside our current radius, so let's look a bit further ahead
            big_step = (self.x + self.radius*2*math.cos(rad_angle),
                        self.y + self.radius*2*math.sin(rad_angle))
            if self.within_bounds(next_step) and self.free_spot(big_step):
                self.location = next_step
            else:
                self.active = False
                if self in circles:
                    circles.remove(self)

            self.angle = (self.angle + self.curve) % 360

        ...

        @staticmethod
        def should_make_baby():
            # 1/50 chance to make a baby
            return not random.randint(0, 20)

        def make_baby(self):
            return Circle(self.radius*.75, self.location)


    for _ in range(10):
        circles.append(Circle(10, (random.randint(0, image_bounds[0]),
                                   random.randint(0, image_bounds[1]))))

    for _ in range(1000):
        for circle in circles:
            circle.draw()
            circle.push()

    image.show()

Not the prettiest thing, but nice and noisey.

.. image:: /images/funkylines.png
    :alt: Some fantastically curvy lines with babies!

We can really start to see a problem with our blank spot checking, we're clearly pushing circles on top of other circles all the time!
Let's fix this by checking a line of pixels in front of us as we step.





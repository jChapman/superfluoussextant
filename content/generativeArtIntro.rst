Generative Art Setup
####################

:date: 2017-03-16
:tags: programming, art, python, PIL, Pillow
:category: programming
:slug: genArtIntro
:header_cover: /images/rootedMoonInverse.png
:status: draft

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

Python, for prototyping it's hard to beat python in terms of speed of development/iteration and available libraries

Pillow, PIL was Python Image Library until it stopped getting updated. Pillow is a fork of PIL that is actively maintained. Pillow allows us to quickly create, edit, and save images.

ImageMagick allows for command line processing of images, in my case I use it mostly for creating GIFs. There are python wrappers for the C++ library, one of the most up to date being `Wand <https://github.com/dahlia/wand>`_

Using the Tools
===============

Here's a rough outline of the steps that my Python script does for each invocation 

1. Create a new folder relative to this script, call it the current date so that the name won't conflict and the folders are in a sane order
2. Copy the current version of this script to the newly created folder, this allows me to jump back to a previous state if I liked the results or if my more recent changes were too drastic 
3. Do the work, for each frame/step draw on a Pillow Image
4. Save the current image, make the name something that will allow for some kind of order
5. Create a file containing the list of all images to be fed to ImageMagick for GIFing
6. Create the GIF



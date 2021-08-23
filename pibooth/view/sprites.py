# -*- coding: utf-8 -*-

""".
"""

import os.path as osp
import pygame
from PIL import Image, ImageOps
from pibooth import fonts
from pibooth import language
from pibooth.pictures import sizing


def get_filename(name):
    """Return absolute path to a picture located in the current package.

    :param name: name of an image located in language folders
    :type name: str

    :return: absolute image path
    :rtype: str
    """
    return osp.join(osp.dirname(osp.abspath(__file__)), 'assets', name)


def colorize_pil_image(pil_image, color, bg_color=None):
    """Convert a picto in white to the corresponding color.

    :param pil_image: PIL image to be colorized
    :type pil_image: :py:class:`PIL.Image`
    :param color: RGB color to convert the picto
    :type color: tuple
    :param bg_color: RGB color to use for the picto's background
    :type bg_color: tuple
    """
    if not bg_color:
        bg_color = (abs(color[0] - 255), abs(color[1] - 255), abs(color[2] - 255))
    _, _, _, alpha = pil_image.split()
    gray_pil_image = pil_image.convert('L')
    new_pil_image = ImageOps.colorize(gray_pil_image, black=bg_color, white=color)
    new_pil_image.putalpha(alpha)
    return new_pil_image


def get_pygame_main_color(surface):
    """Return the main color of the given pygame surface.
    """
    monopixel_surface = pygame.transform.scale(surface, (1, 1))
    return tuple(monopixel_surface.get_at((0, 0)))


def get_pygame_image(name, size=None, antialiasing=True, hflip=False, vflip=False,
                     crop=False, angle=0, color=(255, 255, 255), bg_color=None):
    """Return a Pygame image. If a size is given, the image is
    resized keeping the original image's aspect ratio.

    :param name: name of an image located in language folders
    :type name: str
    :param size: resize image to this size
    :type size: tuple
    :param antialiasing: use antialiasing algorithm when resize
    :type antialiasing: bool
    :param hflip: apply an horizontal flip
    :type hflip: bool
    :param vflip: apply a vertical flip
    :type vflip: bool
    :param crop: crop image to fit aspect ration of the size
    :type crop: bool
    :param angle: angle of rotation of the image
    :type angle: int
    :param color: recolorize the image with this RGB color
    :type color: tuple
    :param bg_color: recolorize the image background with this RGB color
    :type bg_color: tuple

    :return: pygame.Surface with image
    :rtype: object
    """
    path = get_filename(name)
    if not size and not color:
        image = pygame.image.load(path).convert_alpha()
    else:
        if osp.isfile(path):
            pil_image = Image.open(path)
        else:
            pil_image = Image.new('RGBA', size, (0, 0, 0, 0))

        if color:
            pil_image = colorize_pil_image(pil_image, color, bg_color)

        if crop:
            pil_image = pil_image.crop(sizing.new_size_by_croping_ratio(pil_image.size, size))
        pil_image = pil_image.resize(sizing.new_size_keep_aspect_ratio(pil_image.size, size),
                                     Image.ANTIALIAS if antialiasing else Image.NEAREST)

        image = pygame.image.frombuffer(pil_image.tobytes(), pil_image.size, pil_image.mode)

    if hflip or vflip:
        image = pygame.transform.flip(image, hflip, vflip)
    if angle != 0:
        image = pygame.transform.rotate(image, angle)
    return image


def get_pygame_layout_image(text_color, bg_color, layout_number, size):
    """Generate the layout image with the corresponding text.

    :param text_color: RGB color for texts
    :type text_color: tuple
    :param layout_number: number of captures on the layout
    :type layout_number: int
    :param size: maximum size of the layout surface
    :type size: tuple

    :return: surface
    :rtype: :py:class:`pygame.Surface`
    """
    layout_image = get_pygame_image("layout{0}.png".format(layout_number),
                                    size, color=text_color, bg_color=bg_color)
    text = language.get_translated_text(str(layout_number))
    if text:
        rect = layout_image.get_rect()
        rect = pygame.Rect(rect.x + rect.width * 0.3 / 2,
                           rect.y + rect.height * 0.76,
                           rect.width * 0.7, rect.height * 0.20)
        text_font = fonts.get_pygame_font(text, fonts.CURRENT, rect.width, rect.height)
        surface = text_font.render(text, True, bg_color)
        layout_image.blit(surface, surface.get_rect(center=rect.center))
    return layout_image


class Asset(pygame.sprite.DirtySprite):

    def __init__(self):
        super(Asset, self).__init__()
        self.rect = pygame.Rect((0, 0), (10, 10))
        self.image = pygame.Surface(self.rect.size, pygame.SRCALPHA, 32)


class Text(pygame.sprite.DirtySprite):

    def __init__(self):
        super(Text, self).__init__()
        self.rect = pygame.Rect((0, 0), (10, 10))
        self.image = pygame.Surface(self.rect.size, pygame.SRCALPHA, 32)


class Dot(pygame.sprite.DirtySprite):

    def __init__(self):
        super(Dot, self).__init__()
        self.rect = pygame.Rect((0, 0), (10, 10))
        self.image = pygame.Surface(self.rect.size, pygame.SRCALPHA, 32)

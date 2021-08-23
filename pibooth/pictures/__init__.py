# -*- coding: utf-8 -*-

from pibooth.pictures import factory

AUTO = 'auto'
PORTRAIT = 'portrait'
LANDSCAPE = 'landscape'


def get_best_orientation(captures):
    """Return the most adapted orientation (PORTRAIT or LANDSCAPE),
    depending on the resolution of the given captures.

    It use the size of the first capture to determine the orientation.

    :param captures: list of captures to concatenate
    :type captures: list

    :return: orientation PORTRAIT or LANDSCAPE
    :rtype: str
    """
    is_portrait = captures[0].size[0] < captures[0].size[1]
    if len(captures) == 1 or len(captures) == 4:
        if is_portrait:
            orientation = PORTRAIT
        else:
            orientation = LANDSCAPE
    elif len(captures) == 2 or len(captures) == 3:
        if is_portrait:
            orientation = LANDSCAPE
        else:
            orientation = PORTRAIT
    else:
        raise ValueError("List of max 4 pictures expected, got {}".format(len(captures)))
    return orientation


def get_picture_factory(captures, orientation=AUTO, paper_format=(4, 6), force_pil=False, dpi=600):
    """Return the picture factory use to concatenate the captures.

    :param captures: list of captures to concatenate
    :type captures: list
    :param orientation: paper orientation
    :type orientation: str
    :param paper_format: paper size in inches
    :type paper_format: tuple
    :param force_pil: force use PIL implementation
    :type force_pil: bool
    :param dpi: dot-per-inche resolution
    :type dpi: int
    """
    assert orientation in (AUTO, PORTRAIT, LANDSCAPE), "Unknown orientation '{}'".format(orientation)
    if orientation == AUTO:
        orientation = get_best_orientation(captures)

    # Ensure paper format is given in portrait (don't manage orientation with it)
    if paper_format[0] > paper_format[1]:
        paper_format = (paper_format[1], paper_format[0])

    size = (paper_format[0] * dpi, paper_format[1] * dpi)
    if orientation == LANDSCAPE:
        size = (size[1], size[0])

    if not factory.cv2 or force_pil:
        return factory.PilPictureFactory(size[0], size[1], *captures)

    return factory.OpenCvPictureFactory(size[0], size[1], *captures)

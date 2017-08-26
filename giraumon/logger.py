# -*- coding: utf-8 -*-
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl).
import click


def info(message):
    """
    Print message with normal color
    """
    return click.secho(message, bg='black')


def warn(message):
    """
    Print a warning message
    """
    return click.secho(message, bg='black', fg='yellow')

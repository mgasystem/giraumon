# -*- coding: utf-8 -*-
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl).
import click
import time
import os


def _multi_lines(message):
    """
    Split message with new line as an array
    """
    return message.split(os.linesep)


def info(message):
    """
    Print message with normal color
    """
    prefix = '%s %s ' % (time.strftime('%Y-%m-%d %H:%M:%S'),
                          click.style('INFO', fg='green'))
    res = [click.echo(prefix+ click.style(
        l, bg='black')) for l in _multi_lines(message)]
    return '\n'.join(map(str, res))


def warn(message):
    """
    Print a warning message
    """
    prefix = '%s %s ' % (time.strftime('%Y-%m-%d %H:%M:%S'),
                         click.style('WARNING', fg='blue'))
    res = [click.echo(prefix+ click.style(
        l, bg='black')) for l in _multi_lines(message)]
    return '\n'.join(map(str, res))


def error(message):
    """
    Print an error message
    """
    prefix = '%s %s ' % (time.strftime('%Y-%m-%d %H:%M:%S'),
                         click.style('ERROR', fg='red'))
    res = [click.echo(prefix+ click.style(
        l, bg='black')) for l in _multi_lines(message)]
    return '\n'.join(map(str, res))

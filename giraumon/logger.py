# -*- coding: utf-8 -*-
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl).
import click
import time


def info(message):
    """
    Print message with normal color
    """
    prefix = '%s %s ' % (time.strftime('%Y-%m-%d %H:%M:%S'),
                          click.style('INFO', fg='green'))
    return click.echo(prefix+ click.style(message, bg='black'))


def warn(message):
    """
    Print a warning message
    """
    prefix = '%s %s ' % (time.strftime('%Y-%m-%d %H:%M:%S'),
                         click.style('WARNING', fg='blue'))
    return click.echo(prefix+ click.style(message, bg='black'))


def error(message):
    """
    Print an error message
    """
    prefix = '%s %s ' % (time.strftime('%Y-%m-%d %H:%M:%S'),
                         click.style('ERROR', fg='red'))
    return click.echo(prefix+ click.style(message, bg='black'))

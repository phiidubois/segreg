# -*- coding: utf-8 -*-
"""
/***************************************************************************
 segreg
                                 A QGIS plugin
 Compute segregation measures
                             -------------------
        begin                : 2016-02-29
        copyright            : (C) 2016 by Sandro Sousa/UFABC
        email                : sandrofsousa@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load segreg class from file segreg.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .segreg_calc import segreg
    return segreg(iface)

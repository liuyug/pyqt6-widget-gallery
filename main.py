# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause
# from __future__ import annotations

"""PyQt6 port of the widgets/gallery example from Qt v5.15"""

import sys

from PyQt6.QtWidgets import QApplication
from widgetgallery import WidgetGallery


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec())

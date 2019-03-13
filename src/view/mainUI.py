#!/usr/bin/env python3
# vim:fileencoding=utf-8

__license__ = 'GPL v3'
__copyright__ = '2019, Elizeu Xavier <elizeu.xavier at gmail.comt>'

# This file is part of Kinema.

# Kinema is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Kinema is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Kinema.  If not, see <https://www.gnu.org/licenses/>.

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from threading import Thread
from time import sleep
from view.splash import Splash

class MainUI(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)

        # Set position and decoration
        self.set_position(Gtk.WindowPosition.CENTER)
        self.lbl = Gtk.Label()
        self.lbl.set_label("Main window started")
        self.add(self.lbl)
        self.connect('destroy', Gtk.main_quit)

        # Initiate and show the splash screen
        print(("Starting splash"))
        splash = Splash()
        splash.start()

        print(("Simulate MainUI work"))
        sleep(5)

        # Destroy splash
        splash.destroy()
        print(("Splash destroyed"))

        print(("Starting MainUI"))
        self.show_all()
        Gtk.main()
        print(("MainUI ended"))

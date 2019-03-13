#! /usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from threading import Thread



class Splash(Thread):
    def __init__(self):
        super(Splash, self).__init__()

        # Create a popup window
        self.window = Gtk.Window(Gtk.WindowType.POPUP)
        self.window.set_position(Gtk.WindowPosition.CENTER)
        self.window.connect('destroy', Gtk.main_quit)
        self.window.set_default_size(400, 250)

        # Add box and label
        box = Gtk.Box()
        lbl = Gtk.Label()
        lbl.set_label("Kinema is loading...")
        box.pack_start(lbl, True, True, 0)
        self.window.add(box)

    def run(self):
        # Show the splash screen without causing startup notification
        # https://developer.gnome.org/gtk3/stable/GtkWindow.html#gtk-window-set-auto-startup-notification
        self.window.set_auto_startup_notification(False)
        self.window.show_all()
        self.window.set_auto_startup_notification(True)

        # Need to call Gtk.main to draw all widgets
        Gtk.main()

    def destroy(self):
        self.window.destroy()


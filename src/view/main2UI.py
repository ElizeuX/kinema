import sys
import os
import gi
from gi.repository import GdkPixbuf
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gio
from gi.repository import Gtk


# This would typically be its own file
MENU_XML="""
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <menu id="app-menu">   
    <section>
      <item>
        <attribute name="action">app.movieImport</attribute>
        <attribute name="label" translatable="yes">_Importar filmes</attribute>
      </item>
    </section>    
    <section>
      <attribute name="label" translatable="yes">Change label</attribute>
      <item>
        <attribute name="action">win.change_label</attribute>
        <attribute name="target">String 1</attribute>
        <attribute name="label" translatable="yes">String 1</attribute>
      </item>
      <item>
        <attribute name="action">win.change_label</attribute>
        <attribute name="target">String 2</attribute>
        <attribute name="label" translatable="yes">String 2</attribute>
      </item>
      <item>
        <attribute name="action">win.change_label</attribute>
        <attribute name="target">String 3</attribute>
        <attribute name="label" translatable="yes">String 3</attribute>
      </item>
    </section>
    <section>
      <item>
        <attribute name="action">app.preferencia</attribute>
        <attribute name="label" translatable="yes">P_referências</attribute>
      </item>
    </section>
    <section>      
      <item>
        <attribute name="action">app.about</attribute>
        <attribute name="label" translatable="yes">A_juda</attribute>
      </item>
      <item>
        <attribute name="action">app.about</attribute>
        <attribute name="label" translatable="yes">_About</attribute>
      </item>
      <item>
        <attribute name="action">app.quit</attribute>
        <attribute name="label" translatable="yes">_Quit</attribute>
        <attribute name="accel">&lt;Primary&gt;q</attribute>
    </item>
    </section>
  </menu>
</interface>
"""

class AppWindow(Gtk.ApplicationWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_default_size(800, 600)
        #------------------------- TOOLBAR
        # a grid to attach the toolbar
        grid = Gtk.Grid()

        # a toolbar created in the method create_toolbar (see below)
        toolbar = self.create_toolbar()
        # with extra horizontal space
        toolbar.set_hexpand(True)
        # show the toolbar
        toolbar.show()

        # attach the toolbar to the grid
        grid.attach(toolbar, 0, 0, 1, 1)

        # add the grid to the window
        self.add(grid)
        #------------------------

        # This will be in the windows group and have the "win" prefix
        max_action = Gio.SimpleAction.new_stateful("maximize", None,
                                           GLib.Variant.new_boolean(False))
        max_action.connect("change-state", self.on_maximize_toggle)
        self.add_action(max_action)

        # Keep it in sync with the actual state
        self.connect("notify::is-maximized",
                            lambda obj, pspec: max_action.set_state(
                                               GLib.Variant.new_boolean(obj.props.is_maximized)))        
        
        #self.label = Gtk.Label(label=lbl_variant.get_string(),
        #                       margin=30)
        #self.add(self.label)
        #self.label.show()

        


    def on_maximize_toggle(self, action, value):
        action.set_state(value)
        if value.get_boolean():
            self.maximize()
        else:
            self.unmaximize()
   
    #-----------------------
    def create_toolbar(self):
      # a toolbar
      toolbar = Gtk.Toolbar()

      # which is the primary toolbar of the application
      toolbar.get_style_context().add_class(Gtk.STYLE_CLASS_PRIMARY_TOOLBAR)

      # create a button for the "new" action, with a stock image
      new_button = Gtk.ToolButton.new_from_stock(Gtk.STOCK_NEW)
      # label is shown
      new_button.set_is_important(True)
      # insert the button at position in the toolbar
      toolbar.insert(new_button, 0)
      # show the button
      new_button.show()       


      # return the complete toolbar
      return toolbar
    #-----------------------

class Application(Gtk.Application):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="org.example.myapp",
                         flags=Gio.ApplicationFlags.HANDLES_COMMAND_LINE,
                         **kwargs)
        self.window = None
        

        self.add_main_option("test", ord("t"), GLib.OptionFlags.NONE,
                             GLib.OptionArg.NONE, "Command line test", None)       
        
    def do_startup(self):
        Gtk.Application.do_startup(self)

        action = Gio.SimpleAction.new("about", None)
        action.connect("activate", self.on_about)
        self.add_action(action)

        action = Gio.SimpleAction.new("quit", None)
        action.connect("activate", self.on_quit)
        self.add_action(action)

        action = Gio.SimpleAction.new("movieImport", None)
        action.connect("activate", self.on_movieImport)        
        self.add_action(action)

        action = Gio.SimpleAction.new("preferencia", None)
        action.connect("activate", self.on_preferencia)        
        self.add_action(action)

        builder = Gtk.Builder.new_from_string(MENU_XML, -1)
        self.set_app_menu(builder.get_object("app-menu"))

    def do_activate(self):
        # We only allow a single window and raise any existing ones
        if not self.window:
            # Windows are associated with the application
            # when the last one is closed the application shuts down
            self.window = AppWindow(application=self, title="Kinema")

        self.window.present()

    def do_command_line(self, command_line):
        options = command_line.get_options_dict()
        # convert GVariantDict -> GVariant -> dict
        options = options.end().unpack()

        if "test" in options:
            # This is printed on the main instance
            print("Test argument recieved: %s" % options["test"])

        self.activate()
        return 0    

    def on_about(self, action, param):
        about_dialog = Gtk.AboutDialog(transient_for=self.window, modal=True)         
        # lists of authors and documenters (will be used later)
        authors = ["Elizeu Ribeiro Sanches Xavier"]
        documenters = ["Kinema Documentation Team"]
        VERSION = "1.0.1"
        VERSION_NAME = ["VERSÃO DE TESTE"]

        # we fill in the aboutdialog
        about_dialog.set_program_name("Kinema Movie Manager")
        about_dialog.set_copyright( "Copyright \xa9 2019 Elizeu Ribeiro Sanches Xavier")
        about_dialog.set_authors(authors)
        about_dialog.set_documenters(documenters)
        about_dialog.set_website("https://elizeux.github.io/kinema/")
        about_dialog.set_website_label("Kinema Developer Website")
        about_dialog.set_logo(GdkPixbuf.Pixbuf.new_from_file(os.path.join('/home/elizeux/Imagens/', 'pixmaps', 'LpxRf1Pn.jpg')))        
        about_dialog.set_version('%s' % (VERSION))
        data = open('/home/elizeux/Imagens/pixmaps/copyright.txt', 'r').read()
        comment = 'A movie manager for passion'
        about_dialog.set_comments(comment)
        about_dialog.set_license(data)
        about_dialog.present()

    def on_quit(self, action, param):
      self.quit()

    def on_movieImport(self, action, param):      
      dialog = Gtk.FileChooserDialog("Please choose a file", self.window,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

      mfilter = Gtk.FileFilter()
      mfilter.set_name("Video files")
      mfilter.add_mime_type("video/mp4")
      mfilter.add_mime_type("video/mpeg")
      mfilter.add_mime_type("video/ogg")
      mfilter.add_mime_type("video/x-msvideo")
      mfilter.add_mime_type("video/x-matroska")
      mfilter.add_pattern("*.[mM][pP][4]?{a,p,b,r,v}")
      mfilter.add_pattern("*.[mM][1][vV]")
      mfilter.add_pattern("*.[oO][gG][gG]")
      mfilter.add_pattern("*.[aA][vV][iI]")      
      mfilter.add_pattern("*.[mM][kK][vV]")      
      dialog.add_filter(mfilter)

      filter_any = Gtk.FileFilter()
      filter_any.set_name("Any files")
      filter_any.add_pattern("*")
      dialog.add_filter(filter_any)
      
      dialog.show()

      response = dialog.run()     
      if response == Gtk.ResponseType.OK:
        fp = dialog.get_filename()
      
      dialog.destroy()

      #self.addNotebookPage(os.path.basename(fn.get_filename()), text)

    def add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        filter_py = Gtk.FileFilter()
        filter_py.set_name("Python files")
        filter_py.add_mime_type("text/x-python")
        dialog.add_filter(filter_py)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)

    def on_preferencia(self, action, param):
      dialog = DialogPreferencias(self.window)
      response = dialog.run()

      if response == Gtk.ResponseType.OK:
        print("The OK button was clicked")
        dialog = Gtk.MessageDialog(self.window, 0, Gtk.MessageType.INFO,
            Gtk.ButtonsType.OK, "The OK button was clicked")
        dialog.format_secondary_text(
            "And this is the secondary text that explains things.")
        dialog.run()
        print("INFO dialog closed")

        dialog.destroy()
      elif response == Gtk.ResponseType.CANCEL:
        print("The Cancel button was clicked")

      dialog.destroy()

       
class DialogPreferencias(Gtk.Dialog):

    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Preferências", parent, 0,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OK, Gtk.ResponseType.OK))

        self.set_default_size(250, 200)

        label = Gtk.Label("This is a dialog to display additional information")

        box = self.get_content_area()
        box.add(label)
        self.show_all()

if __name__ == "__main__":
    app = Application()
    app.run(sys.argv)

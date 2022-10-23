class Viewer:
    def set_current_scene(self, text_desc, bg_pic, options):
        pass

    def selected_option(self):
        """Return false if not selected yet, otherwise a number."""
        return False

class CliViewer(Viewer):
    def set_current_scene(self,text_desc,bg_pic,options):
        print(text_desc)
        for ix, val in enumerate(options):
            print(f"{ix+1}. {val}")

    def selected_option(self):
        """Returns an option index"""
        s = input("Select an option:")
        n = int(s)
        return n-1


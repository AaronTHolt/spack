from spack import *

class Emacs(Package):
    """The Emacs programmable text editor."""
    homepage = "https://www.gnu.org/software/emacs"
    url      = "http://ftp.gnu.org/gnu/emacs/emacs-24.5.tar.gz"

    version('24.5', 'd74b597503a68105e61b5b9f6d065b44')

    depends_on('ncurses')
    # Emacs also depends on:
    #     GTK or other widget library
    #     libtiff, png, etc.
    # For now, we assume the system provides all that stuff.
    # For Ubuntu 14.04 LTS:
    #     sudo apt-get install libgtk-3-dev libxpm-dev libtiff5-dev libjpeg8-dev libgif-dev libpng12-dev

    def install(self, spec, prefix):
        configure('--prefix=%s' % prefix)
        make()
        make("install")

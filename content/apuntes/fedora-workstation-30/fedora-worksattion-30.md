Title: Instalación de Fedora Workstation 30
Slug: fedora-workstation-30
Summary: Comandos de instalación del software (preferido por el autor) en Fedora Workstation 30 con KDE.
Tags: fedora, gnu linux
Date: 2019-08-13 19:32
Modified: 2019-08-13 19:32
Category: apuntes
Preview: preview.png
Image: imagen.jpg


En este apunte es una actualización de [Fedora Workstation 29 con KDE parte 2]({filename}/apuntes/fedora-workstation-29-parte-02/fedora-workstation-29-parte-02.md).

Luego de instalar Fedora con KDE con una memoria USB y eligiendo el entorno gráfico KDE; hacemos una actualización...

    # dnf --refresh check-update
    # dnf update

Y reiniciamos...

    # systemctl reboot

Instale LibreOffice...

    # dnf group install --with-optional LibreOffice
    # dnf install libreoffice-help-es libreoffice-langpack-es

Instale LaTeX...

    # dnf install texlive-scheme-tetex
    # dnf install texlive-collection-latexextra
    # dnf install texlive-collection-pstricks
    # dnf install texlive-babel-spanish texlive-babel-spanish-doc texlive-hyphen-spanish
    # dnf install texlive-babel-english texlive-babel-english-doc texlive-hyphen-english

Instale Python...

    # dnf group install --with-optional "Python Classroom"
    # dnf group install --with-optional "Python Science"

Instale utilerías diversas...

    # dnf install system-storage-manager
    # dnf install pwgen youtube-dl hwinfo

Instale software de KDE...

    # dnf install kate filelight umbrello krename okular texstudio

Instale soporte para impresoras HP...

    # dnf install hplip

Instale GIMP...

    # dnf install gimp

Instale Inkscape...

    # dnf install inkscape

Instale Calibre...

    # dnf install calibre

Instale tipografías...

    # dnf install liberation-fonts
    # dnf install bitstream-vera-sans-fonts bitstream-vera-serif-fonts bitstream-vera-sans-mono-fonts
    # dnf install terminus-fonts

Prepare los repositorios adicionales...

    # dnf install fedora-workstation-repositories
    # dnf update
    # dnf repolist --all

Instale Google Chrome y sus tipografías...

    # dnf config-manager --set-enabled google-chrome
    # dnf update
    # dnf install google-chrome-stable
    # dnf install google-droid-sans-fonts google-droid-sans-mono-fonts google-droid-serif-fonts
    # dnf install google-noto-sans-fonts google-noto-sans-mono-fonts google-noto-serif-fonts
    # dnf install google-roboto-fonts google-roboto-condensed-fonts

Configure los repositorios RPM Fusion...

    # dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm \
      https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
    # dnf update

Instale más programas de RPM Fusion...

    # dnf install fuse-exfat exfat-utils
    # dnf install ffmpeg ffmpegthumbs
    # dnf install mplayer mencoder
    # dnf install audacity-freeworld
    # dnf install kdenlive frei0r-plugins
    # dnf install moc
    # dnf groupupdate Multimedia

Instale Sublime Text a partir de su propio repositorio...

    # rpm -v --import https://download.sublimetext.com/sublimehq-rpm-pub.gpg
    # dnf config-manager --add-repo https://download.sublimetext.com/rpm/stable/x86_64/sublime-text.repo
    # dnf update
    # dnf install sublime-text

Instale Libvirtd...

    # dnf group install 'Virtualización' --with-optional

Instale los reproductores de multimedia VLC y MPV

    # dnf install vlc
    # dnf install mpv

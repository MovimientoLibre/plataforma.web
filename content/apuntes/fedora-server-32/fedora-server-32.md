Title: Instalación de Fedora Server 32
Slug: fedora-server-32
Summary: Instalación de un equipo para hacer respaldos.
Tags: fedora, gnu linux, servidores, software libre
Date: 2019-09-26 18:48
Modified: 2019-09-26 18:48
Category: apuntes
Preview: fedora-logo-icon.png
Status: draft


Preparar la memoria USB con el instalador

    $ sudo fdisk -l /dev/sdc
    $ sudo dd if=Fedora-Server-netinst-x86_64-32-1.6.iso of=/dev/sdc
    $ sudo sync

El servidor tiene 1 GB de RAM y no puede con la instalación Gráfica de Anaconda, asi que

- Inserte la memoria USB en el servidor
- Reinice
- Cuando aparezca el GRUB presione TAB
- Elija Install Fedora 32
- Agregue `inst.text` al final de los parámetros del kernel
- Presione ENTER


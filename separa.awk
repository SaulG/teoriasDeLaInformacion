#!/usr/bin/awk -f
{
    if ($4 == seleccionado) {
        print $0
    }
}
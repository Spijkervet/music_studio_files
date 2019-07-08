#!/usr/bin/python
import os
import sys
import subprocess

def install(file_path):
    print('\n### INSTALLING ###\n{}\n'.format(file_path))
    os.system('sudo installer -verbose -allowUntrusted -pkg "{}" -target /'.format(file_path))

def install_dmg(path):
    print('\n### INSTALLING ###\n{}\n'.format(file_path))
    os.system('sudo ./install_dmg.sh "{}"'.format(file_path))

def install_fabfilter(path):
    print('### INSTALLING FABFILTER ###')
    components = os.path.join(path, 'Components')
    vst = os.path.join(path, 'VST')

    vst_out = os.path.join(PLUGINS_DIR, 'VST', 'FabFilter')
    os.system('sudo cp -a "{}" "{}"'.format(components, PLUGINS_DIR))
    os.system('sudo cp -a "{}" "{}"'.format(vst, vst_out))

def install_spire(path):
    component = os.path.join(path, 'Spire-1.1.component')
    vst = os.path.join(path, 'Spire-1.1.vst')
    os.system('sudo cp -a "{}" {}'.format(component, COMPONENTS_DIR))
    os.system('sudo cp -a "{}" {}'.format(vst, VST_DIR))

def install_arturia(path):
    command = os.path.join(path, 'Arturia_V_Collection_6_Patch_v3.command')
    subprocess.call(command)


if __name__ == '__main__':
    PLUGINS_DIR = '/Library/Audio/Plug-Ins'
    COMPONENTS_DIR = os.path.join(PLUGINS_DIR, 'Components')
    VST_DIR = os.path.join(PLUGINS_DIR, 'VST')

    walk_dir = 'vst/macOS'
    fab_filter_dir = os.path.abspath(os.path.join(walk_dir, 'FabFilter2019'))
    spire_dir = os.path.abspath(os.path.join(walk_dir, 'Spire'))
    arturia_dir = os.path.abspath(os.path.join(walk_dir, 'ArturiaVCollection6'))
    for root, subdirs, files in os.walk(walk_dir):
        for filename in files:
            file_path = os.path.join(root, filename)
            ext = file_path.split('.')[-1]
            if ext == 'pkg' or ext == 'mpkg':
                install(file_path)
            if ext == 'dmg':
                install_dmg(file_path)

    install_fabfilter(fab_filter_dir)
    install_spire(spire_dir)
    install_arturia(arturia_dir)

    print('### INSTALLATION COMPLETE ###')

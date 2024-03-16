# -*- mode: python ; coding: utf-8 -*-
import os
from kivy.deps import sdl2, glew

a = Analysis(
    ['main.py'],
    pathex=['/home/spiced/Downloads/'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

a.datas += [('Code\\converter.kv',
'\\kivy_venv\\converter.kv',
'DATA')]

exe = EXE(exe,
    Tree('kivy_venv\\'),
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    *[Tree(p) for p in
    (sdl2.dep_bins +
    glew.dep_bins)],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

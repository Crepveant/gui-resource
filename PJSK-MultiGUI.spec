# -*- mode: python ; coding: utf-8 -*-
import os
import janome

janome_base = os.path.dirname(janome.__file__)
janome_sysdic = os.path.join(janome_base, 'sysdic')

datas = [
    (janome_sysdic, 'janome/sysdic'),
    ('commons.py', '.')
]

a = Analysis(
    ['PJSK-MultiGUI.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'matplotlib.tests',
        'numpy.random._examples',
    ],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='PJSK-MultiGUI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['favicon.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PJSK-MultiGUI',
)
app = BUNDLE(
    coll,
    name='PJSK-MultiGUI.app',
    icon='favicon.ico',
    bundle_identifier=None,
)

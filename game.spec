# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
py_files = [
    'ChessAI.py',
    'consts.py',
    'game.py',
    'gobang.py',
    'escmenu.py',
    'Mainmenu.py',
    'read.py',
    'render.py',
    'save.py'
]
add_files = [
    ('UI\\*.png', 'UI'),
    ('UI\\*.jpg', 'UI'),
    ('UI\\*.wav', 'UI')
]
a = Analysis(py_files,
             pathex=['C:\\Users\\86155\\Desktop\\新建文件夹'],
             binaries=[],
             datas=add_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['zmq'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='五子棋',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          )
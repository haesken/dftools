# -*- mode: python -*-
a = Analysis(['../../init_editor.py'],
             pathex=['/home/mike/games/dwarf_fortress_auto/develop/pyinstaller'],
             hiddenimports=[],
             hookspath=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'init_editor'),
          debug=False,
          strip=None,
          upx=True,
          console=True )

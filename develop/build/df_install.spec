# -*- mode: python -*-
a = Analysis(['../../df_install.py'],
             pathex=['../../modules/', '/home/mike/games/dwarf_fortress_auto/develop/pyinstaller'],
             hiddenimports=[],
             hookspath=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'df_install'),
          debug=False,
          strip=None,
          upx=True,
          console=True )

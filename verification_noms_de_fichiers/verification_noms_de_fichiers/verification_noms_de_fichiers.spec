# -*- mode: python -*-

block_cipher = None


a = Analysis(['verification_noms_de_fichiers.py'],
             pathex=['C:\\Users\\Lully\\Documents\\Hélène\\scripts\\mn\\verification_noms_de_fichiers\\verification_noms_de_fichiers'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='verification_noms_de_fichiers',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='verification_noms_de_fichiers')

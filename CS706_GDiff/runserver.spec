# -*- mode: python -*-

block_cipher = None

def addTranslations():
    import os
    extraDatas = []
    for file in os.listdir('StructOpt/static/css'):
        
        extraDatas.append(('static/css/'+file, 'StructOpt/static/css/' + file, 'DATA'))
        
    for file in os.listdir('StructOpt/static/fonts'):
        extraDatas.append(('static/fonts/'+file, 'StructOpt/static/fonts/' + file, 'DATA'))
        
    for file in os.listdir('StructOpt/static/images'):
        extraDatas.append(('static/images/'+file, 'StructOpt/static/images/' + file, 'DATA'))
        
    for file in os.listdir('StructOpt/static/js'):
        extraDatas.append(('static/js/'+file, 'StructOpt/static/js/' + file, 'DATA'))    

    for file in os.listdir('StructOpt/templates'):
            extraDatas.append(('templates/'+file, 'StructOpt/templates/' + file, 'DATA'))
    
    for file in os.listdir('StructOpt/models'):
            extraDatas.append(('models/'+file, 'StructOpt/models/' + file, 'DATA'))
    
    for file in os.listdir('input'):
            extraDatas.append((file, 'input/' + file, 'DATA'))
    
    for file in os.listdir('output'):
            extraDatas.append((file, 'output/' + file, 'DATA'))

    print "extraDatas = ", extraDatas
    return extraDatas

a = Analysis(['runserver.py'],
             pathex=['/Users/mehreenali/Documents/workspace/StructOpt'],
             binaries=None,
             datas= None,
             hiddenimports=["flask",
         "flask_restful",
         "flask_sqlalchemy",
         "flask.views","flask_restful.views"],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             win_no_prefer_redirects=None,
             win_private_assemblies=None,
             cipher=block_cipher)

# append the translations directory
a.datas += addTranslations()

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='runserver',
          debug=False,
          strip=None,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='runserver')
if sys.platform == 'darwin':
   app = BUNDLE(exe,
                name=‘.app',
                icon=None)
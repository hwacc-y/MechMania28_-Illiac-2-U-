import zipapp
print("Writing to bot.pyz...")
<<<<<<< HEAD
zipapp.create_archive('.', main='main:main', target='bot.pyz')
=======
zipapp.create_archive('.', main='main:main', target='../bot.pyz')
>>>>>>> slink_up
print("Done!")
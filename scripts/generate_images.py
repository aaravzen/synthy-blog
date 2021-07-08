import os

image_album = raw_input()
path = 'static/images/%s' % image_album

for image_name in os.listdir(path):
    print("![%s](/images/%s/%s?resize=1200 '%s')" % (image_name, image_album, image_name, image_name))
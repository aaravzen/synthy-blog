import os

image_album = raw_input()
path = 'static/images/%s' % image_album

for image_name in os.listdir(path):
    print("![%s](/images/%s/%s.jpg?resize=600 '%s')" % (image_name, image_album, image_name, image_name))
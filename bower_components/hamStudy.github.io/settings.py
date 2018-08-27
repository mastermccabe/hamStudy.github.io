DEBUG = False
ALLOWED_HOSTS = ['{{yourEC2.public.ip}}']
# add the line below to the bottom of the file
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

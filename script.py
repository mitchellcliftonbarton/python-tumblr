import pytumblr
import os
# import oauth2
# from tumblr_keys import *    #this imports the content in our tumblr_keys.py file

# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
  'OwkaLncuZlxDpofwTpcfCz87kEIEuWRRjEpl0i2tvRWLpVTeJX',
  'QooQH16tPvKNmGjFK5l2fHeMdIyoWd4p6FNkhVlXenivh3fPSt',
  'lXZMoziJiSDpEPzJYoHTEhMNFFt12emtiAJfvq6EBMf7bFglSt',
  'LGeRorUaZFZeBdfwB7D0sNkp6nCMcr4MNZ455DZ9bjGAhsAQ1e'
)

client.info()


#Posts an image to your tumblr.
#Make sure you point an image in your hard drive. Here, 'image.jpg' must be in the
#same folder where your script is saved.
#From yourBlogName.tumblr.com should just use 'yourBlogName'
#The default state is set to "queue", to publish use "published"

for filename in os.listdir('images/'):
    if filename.endswith(".jpg"):
        # print(os.path.join(directory, filename))
        print('images/' + filename)
        client.create_photo('black-sand-white-sand-grey-sand', state="published", data='images/' + filename)
        # continue
    else:
        print('poop')
        # continue

# client.create_photo('black-sand-white-sand-grey-sand', state="published", tags=["testing", "ok"], data="images/")

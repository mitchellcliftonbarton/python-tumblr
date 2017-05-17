# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
  'OwkaLncuZlxDpofwTpcfCz87kEIEuWRRjEpl0i2tvRWLpVTeJX',
  'QooQH16tPvKNmGjFK5l2fHeMdIyoWd4p6FNkhVlXenivh3fPSt',
  'lXZMoziJiSDpEPzJYoHTEhMNFFt12emtiAJfvq6EBMf7bFglSt',
  'LGeRorUaZFZeBdfwB7D0sNkp6nCMcr4MNZ455DZ9bjGAhsAQ1e'
)

# Make the request
client.info()

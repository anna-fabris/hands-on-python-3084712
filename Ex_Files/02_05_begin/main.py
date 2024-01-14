import os # importing the os module

DEVELOPMENT = "development"
PRODUCTION = "production"
STAGING = "staging"
CODE_SPACE = "code_space"
LOCAL = "local"
# os.environ.get to access the env I am running on and grab things from there
current_env = os.environ.get("ENV_NAME", DEVELOPMENT)

if current_env == DEVELOPMENT:
    print("Development environment")
elif current_env == PRODUCTION:
    print("Production environment")
elif current_env == STAGING:
    print("Staging environment")
elif current_env in [CODE_SPACE, LOCAL]: # you can put a collection
    print("Codespace or local environment")
else:
    print("Unknown environment")
# if you 'fake' to change the env
# f.e. export ENV_NAME="local"
# you get a different result
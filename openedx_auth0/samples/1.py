from django.conf import settings

settings.configure(FEATURES={"AUTH0_DOMAIN": "dev-ega1x8jg.us"})
print(settings.FEATURES.get("AUTH0_DOMAIN"))
print(settings.FEATURES.get("AUTH0_DOMAIN", u"auth0.com"))
print(u"auth0.com")
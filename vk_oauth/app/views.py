from django.shortcuts import render

from . import api_vk


def vk_friends(request):
    """
    Generate html page.

    Page contains information about authorized user and his 5 random friends.
    """
    context = {}
    user = request.user

    if user.is_authenticated:
        user_social_auth = user.social_auth.get(provider='vk-oauth2')
        access_token = user_social_auth.access_token

        api = api_vk.get_vk_api(access_token)
        friends_info = api_vk.get_vk_friends(api)
        account_info = api_vk.get_account_info(api)

        context.update({
            "account_info": account_info,
            "friends_info": friends_info,
        })

    return render(request, "vk_friends.html", context)

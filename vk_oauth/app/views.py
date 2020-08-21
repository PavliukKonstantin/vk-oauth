import vk_api
from django.shortcuts import render


def get_vk_api(access_token):
    vk_session = vk_api.VkApi(token=access_token)
    api = vk_session.get_api()
    return api


def get_account_info(api):
    account_info = api.users.get(
        fields=["photo_200_orig"],
    )
    return account_info


def get_vk_friends(api):
    five_friends = api.friends.get(
        order='random',
        count=5,
        fields=["photo_200_orig"],
    )
    return five_friends.get("items")


def index(request):
    context = {}
    user = request.user
    # if user.is_authenticated:
    #     user_methods = user.__dir__

    #     context.update({
    #         'first_name': user.first_name,
    #         'last_name': user.last_name,
    #         'email': user.email,
    #         "user_methods": user_methods,
    #     })

    if user.is_authenticated:
        user_social_auth = user.social_auth.get(provider='vk-oauth2')
        access_token = user_social_auth.access_token

        api = get_vk_api(access_token)
        vk_friends = get_vk_friends(api)
        account_info = get_account_info(api)[0]
        # user_data = get_user_data(api)

        context.update({
            "account_info": account_info,
            "vk_friends": vk_friends,
        })

    return render(request, "index.html", context)

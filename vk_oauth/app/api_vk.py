import vk_api


def get_vk_api(access_token: str) -> vk_api.VkApi:
    """
    Return API session.

    Args:
        access_token (str): access token VK application.

    Returns:
        vk_api.VkApi: session for API methods use.
    """
    vk_session = vk_api.VkApi(token=access_token)
    api = vk_session.get_api()
    return api


def get_account_info(api: vk_api.VkApi) -> dict:
    """
    Return authorized account information.

    Args:
        api (vk_api.VkApi): session for API methods use.

    Returns:
        dict: authorized account information.
    """
    account_info = api.users.get(
        fields=["photo_200_orig"],
    )
    return account_info[0]


def get_vk_friends(api: vk_api.VkApi) -> dict:
    """
    Return information about 5 random friends.

    Args:
        api (vk_api.VkApi): session for API methods use.

    Returns:
        dict: information about 5 random friends.
    """
    friends_info = api.friends.get(
        order="random",
        count=5,
        fields=["photo_200_orig"],
    )
    return friends_info.get("items")

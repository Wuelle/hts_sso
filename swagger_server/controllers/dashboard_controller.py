import connexion
import six

from swagger_server.models.dashboard_get_user_info_body import DashboardGetUserInfoBody  # noqa: E501
from swagger_server.models.dashboard_info_container import DashboardInfoContainer  # noqa: E501
from swagger_server.models.dashboard_info import DashboardInfo  # noqa: F401,E501
from swagger_server import util

from swagger_server.models.account_info import AccountInfo  # noqa: F401,E501
from swagger_server.models.privacy_settings import PrivacySettings  # noqa: F401,E501
from swagger_server.models.route_category import RouteCategory  # noqa: F401,E501
from swagger_server.models.privacy_setting import PrivacySetting  # noqa: F401,E501
from swagger_server.models.linked_accounts import LinkedAccounts  # noqa: F401,E501
from swagger_server.models.linked_account import LinkedAccount  # noqa: F401,E501



def dashboard_get_user_info(body):  # noqa: E501
    """Get a users account data

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: DashboardInfoContainer
    """
    if connexion.request.is_json:
        body = DashboardGetUserInfoBody.from_dict(connexion.request.get_json())  # noqa: E501
    allowed_routes = []
    account_info = AccountInfo(
        account_name="Wuelle",
        display_name="Alaska",
        joined="1. Feb. 2010",
        last_login="1. Feb. 2010",
        email="foo@example.com",
        website="http://example.com",
        timezone=3,
        avatar_url="https://www.hackthissite.org/pages/user/avatar.view.php?id=standard/terrora.jpg",
        about_me="Hi! I am Alaska!",
        linked_accounts=LinkedAccounts(
            github=LinkedAccount(name="Wuelle", href="https://github.com/wuelle/"),
            discord=LinkedAccount(name="Alaska#4736", href="https://discord.com/users/549668688593289248"),
        ),
    )
    privacy_settings = PrivacySettings(
        email=PrivacySetting(hidden_from_discord=False, hidden_from_profile=True),
        irc_nicks=PrivacySetting(hidden_from_discord=True, hidden_from_profile=True),
        linked_discord_accounts=PrivacySetting(hidden_from_discord=False, hidden_from_profile=False),
    )
    content = DashboardInfo(allowed_routes=allowed_routes, account_info=account_info, privacy_settings=privacy_settings)
    return DashboardInfoContainer(nonce="abc", content=content)

# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.dashboard_info_children import DashboardInfoChildren  # noqa: F401,E501
from swagger_server import util


class RouteCategory(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, children: List[DashboardInfoChildren]=None):  # noqa: E501
        """RouteCategory - a model defined in Swagger

        :param name: The name of this RouteCategory.  # noqa: E501
        :type name: str
        :param children: The children of this RouteCategory.  # noqa: E501
        :type children: List[DashboardInfoChildren]
        """
        self.swagger_types = {
            'name': str,
            'children': List[DashboardInfoChildren]
        }

        self.attribute_map = {
            'name': 'name',
            'children': 'children'
        }
        self._name = name
        self._children = children

    @classmethod
    def from_dict(cls, dikt) -> 'RouteCategory':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RouteCategory of this RouteCategory.  # noqa: E501
        :rtype: RouteCategory
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this RouteCategory.


        :return: The name of this RouteCategory.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this RouteCategory.


        :param name: The name of this RouteCategory.
        :type name: str
        """

        self._name = name

    @property
    def children(self) -> List[DashboardInfoChildren]:
        """Gets the children of this RouteCategory.


        :return: The children of this RouteCategory.
        :rtype: List[DashboardInfoChildren]
        """
        return self._children

    @children.setter
    def children(self, children: List[DashboardInfoChildren]):
        """Sets the children of this RouteCategory.


        :param children: The children of this RouteCategory.
        :type children: List[DashboardInfoChildren]
        """

        self._children = children

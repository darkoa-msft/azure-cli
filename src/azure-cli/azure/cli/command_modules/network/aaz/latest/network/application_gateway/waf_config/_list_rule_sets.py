# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network application-gateway waf-config list-rule-sets",
)
class ListRuleSets(AAZCommand):
    """Get information on available WAF rule sets, rule groups, and rule IDs.

    :example: List available rule groups in OWASP type rule sets.
        az network application-gateway waf-config list-rule-sets --type OWASP

    :example: List available rules in the OWASP 3.0 rule set.
        az network application-gateway waf-config list-rule-sets --group '*' --type OWASP --version 3.0

    :example: List available rules in the `crs_35_bad_robots` rule group.
        az network application-gateway waf-config list-rule-sets --group crs_35_bad_robots

    :example: List available rules in table format.
        az network application-gateway waf-config list-rule-sets -o table
    """

    _aaz_info = {
        "version": "2022-05-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.network/applicationgatewayavailablewafrulesets", "2022-05-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ApplicationGatewaysListAvailableWafRuleSets(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ApplicationGatewaysListAvailableWafRuleSets(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/providers/Microsoft.Network/applicationGatewayAvailableWafRuleSets",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-05-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType()
            _element.location = AAZStrType()
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.rule_groups = AAZListType(
                serialized_name="ruleGroups",
                flags={"required": True},
            )
            properties.rule_set_type = AAZStrType(
                serialized_name="ruleSetType",
                flags={"required": True},
            )
            properties.rule_set_version = AAZStrType(
                serialized_name="ruleSetVersion",
                flags={"required": True},
            )
            properties.tiers = AAZListType()

            rule_groups = cls._schema_on_200.value.Element.properties.rule_groups
            rule_groups.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.rule_groups.Element
            _element.description = AAZStrType()
            _element.rule_group_name = AAZStrType(
                serialized_name="ruleGroupName",
                flags={"required": True},
            )
            _element.rules = AAZListType(
                flags={"required": True},
            )

            rules = cls._schema_on_200.value.Element.properties.rule_groups.Element.rules
            rules.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.rule_groups.Element.rules.Element
            _element.action = AAZStrType()
            _element.description = AAZStrType()
            _element.rule_id = AAZIntType(
                serialized_name="ruleId",
                flags={"required": True},
            )
            _element.rule_id_string = AAZStrType(
                serialized_name="ruleIdString",
            )
            _element.state = AAZStrType()

            tiers = cls._schema_on_200.value.Element.properties.tiers
            tiers.Element = AAZStrType()

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ListRuleSetsHelper:
    """Helper class for ListRuleSets"""


__all__ = ["ListRuleSets"]

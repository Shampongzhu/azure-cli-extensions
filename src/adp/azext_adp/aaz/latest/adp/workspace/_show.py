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
    "adp workspace show",
)
class Show(AAZCommand):
    """Get a Workspace

    :example: show workspace in resource group
        az adp workspace show --subscription sample-subscription --resource-group sample-rg --name sample-ws
    """

    _aaz_info = {
        "version": "2022-09-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.autonomousdevelopmentplatform/workspaces/{}", "2022-09-01-preview"],
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

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.workspace_name = AAZStrArg(
            options=["-n", "--name", "--workspace-name"],
            help="Workspace Name",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[a-z0-9][-a-z0-9]{0,45}$",
                max_length=46,
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.WorkspacesGet(ctx=self.ctx)()

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class WorkspacesGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AutonomousDevelopmentPlatform/workspaces/{workspaceName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "workspaceName", self.ctx.args.workspace_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-09-01-preview",
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
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.identity = AAZObjectType()
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200.identity
            identity.identity = AAZObjectType()

            identity = cls._schema_on_200.identity.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType(
                flags={"required": True},
            )
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200.identity.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType()

            _element = cls._schema_on_200.identity.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
                flags={"read_only": True},
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.auto_generated_domain_name_label_scope = AAZStrType(
                serialized_name="autoGeneratedDomainNameLabelScope",
            )
            properties.batch_accounts = AAZListType(
                serialized_name="batchAccounts",
            )
            properties.data_catalog = AAZObjectType(
                serialized_name="dataCatalog",
            )
            properties.data_location = AAZStrType(
                serialized_name="dataLocation",
            )
            properties.direct_read_access = AAZStrType(
                serialized_name="directReadAccess",
            )
            properties.encryption = AAZObjectType()
            properties.endpoint = AAZStrType(
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.resim = AAZObjectType()
            properties.source_resource_id = AAZStrType(
                serialized_name="sourceResourceId",
            )
            properties.storage_account_count = AAZIntType(
                serialized_name="storageAccountCount",
            )
            properties.storage_sku = AAZObjectType(
                serialized_name="storageSku",
            )

            batch_accounts = cls._schema_on_200.properties.batch_accounts
            batch_accounts.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.batch_accounts.Element
            _element.batch_account_resource_id = AAZStrType(
                serialized_name="batchAccountResourceId",
                flags={"required": True},
            )
            _element.user_assigned_identity_resource_id = AAZStrType(
                serialized_name="userAssignedIdentityResourceId",
            )

            data_catalog = cls._schema_on_200.properties.data_catalog
            data_catalog.data_explorer = AAZObjectType(
                serialized_name="dataExplorer",
            )
            data_catalog.external_workspace_ids = AAZListType(
                serialized_name="externalWorkspaceIds",
            )
            data_catalog.state = AAZStrType(
                flags={"required": True},
            )

            data_explorer = cls._schema_on_200.properties.data_catalog.data_explorer
            data_explorer.azure_sku = AAZObjectType(
                serialized_name="azureSku",
                flags={"required": True, "client_flatten": True},
            )

            azure_sku = cls._schema_on_200.properties.data_catalog.data_explorer.azure_sku
            azure_sku.capacity = AAZIntType()
            azure_sku.name = AAZStrType()
            azure_sku.tier = AAZStrType()

            external_workspace_ids = cls._schema_on_200.properties.data_catalog.external_workspace_ids
            external_workspace_ids.Element = AAZStrType()

            encryption = cls._schema_on_200.properties.encryption
            encryption.customer_managed_key_encryption = AAZObjectType(
                serialized_name="customerManagedKeyEncryption",
                flags={"client_flatten": True},
            )

            customer_managed_key_encryption = cls._schema_on_200.properties.encryption.customer_managed_key_encryption
            customer_managed_key_encryption.key_encryption_key_identity = AAZObjectType(
                serialized_name="keyEncryptionKeyIdentity",
                flags={"required": True, "client_flatten": True},
            )
            customer_managed_key_encryption.key_encryption_key_url = AAZStrType(
                serialized_name="keyEncryptionKeyUrl",
                flags={"required": True},
            )

            key_encryption_key_identity = cls._schema_on_200.properties.encryption.customer_managed_key_encryption.key_encryption_key_identity
            key_encryption_key_identity.user_assigned_identity_resource_id = AAZStrType(
                serialized_name="userAssignedIdentityResourceId",
                flags={"required": True},
            )

            resim = cls._schema_on_200.properties.resim
            resim.state = AAZStrType(
                flags={"required": True},
            )

            storage_sku = cls._schema_on_200.properties.storage_sku
            storage_sku.name = AAZStrType(
                flags={"required": True},
            )

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
                flags={"read_only": True},
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
                flags={"read_only": True},
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
                flags={"read_only": True},
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
                flags={"read_only": True},
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
                flags={"read_only": True},
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
                flags={"read_only": True},
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


__all__ = ["Show"]

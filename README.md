# Aserto Authorizer gRPC client
This is an automatically generated client for interacting with Aserto's [Authorizer service](https://docs.aserto.com/docs/authorizer-guide/overview) using the gRPC protocol.

## Installation
### Using Pip
```sh
pip install aserto-authorizer
```
### Using Poetry
```sh
poetry add aserto-authorizer
```
## Usage
```py
from aserto_authorizer.aserto.authorizer.v2.api import (
    IdentityContext,
    IdentityType,
    PolicyContext,
)
from aserto_authorizer.aserto.authorizer.v2 import (
    AuthorizerStub,
    DecisionTreeOptions,
    DecisionTreeResponse,
    PathSeparator,
)
from grpclib.client import Channel


async with Channel(host=host, port=port, ssl=True) as channel:
    headers = {
        "authorization": f"basic {ASERTO_API_KEY}"
    }

    client = AuthorizerStub(channel, metadata=headers)

    response = await client.decision_tree(
        policy_context=PolicyContext(
            name=ASERTO_POLICY_NAME,
            path=ASERTO_POLICY_PATH_ROOT,
            decisions=["visible", "enabled", "allowed"],
        ),
        identity_context=IdentityContext(type=IdentityType.IDENTITY_TYPE_NONE),
        resource_context=Proto.Struct(),
        options=DecisionTreeOptions(
            path_separator=PathSeparator.PATH_SEPARATOR_DOT,
        ),
    )

    assert response == DecisionTreeResponse(
        path_root=ASERTO_POLICY_PATH_ROOT,
        path=Proto.Struct(
            fields={
                "GET.your.policy.path": Proto.Value(
                    struct_value=Proto.Struct(
                        fields={
                            "visible": Proto.Value(bool_value=True),
                            "enabled": Proto.Value(bool_value=True),
                            "allowed": Proto.Value(bool_value=False),
                        },
                    ),
                ),
            },
        ),
    )
```
import graphene


class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, info):
        return 'Mabuhay! Welcome to Netong\'s Bahay Kubo!'


schema = graphene.Schema(query=Query)

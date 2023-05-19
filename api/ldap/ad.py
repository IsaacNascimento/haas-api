from ldap3 import ALL, ALL_ATTRIBUTES, Connection, Server
from ldap3.core.exceptions import LDAPException

from ldap.schemas import UsuarioSchemaAll
from ldap.config import settings




# por padrao a conexao vai ser sempre usando SSL
_use_ssl = True


def consultar_ad(email: str, senha: str) -> UsuarioSchemaAll:

    try:
        server = Server(host=settings.LDAP_HOST, port=settings.LDAP_PORT,
                        use_ssl=settings.LDAP_USE_SSL, get_info=ALL)

        connection = Connection(server=server, user="{dominio}{user}".format(dominio=settings.LDAP_DOMINIO_LOGIN, user=email),
                                password=senha, authentication="SIMPLE", auto_bind=True, read_only=True)

        if connection.bind():
            user = email
            result = connection.search(
                search_base=settings.LDAP_SEARCH_BASE,
                search_filter=f'(sAMAccountName={user})',
                attributes=['mail', 'sAMAccountName'])

            if result:
                attributes = connection.response[0]['attributes']

            connection.unbind()
    except LDAPException:
        return None
    else:
        usuario: UsuarioSchemaAll = UsuarioSchemaAll(
            email = attributes['mail'],
            usuario=attributes['sAMAccountName'])

        return usuario

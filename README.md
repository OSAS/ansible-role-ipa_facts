This role add a module ipa_facts who provides several facts on
a enrolled IPA system, by parsing the ipa configuration file.

# Usage

In order to use it, just include the role, and it will automatically
gather facts.

# Return values

The ipa_facts module will return several values:

* ipa_realm, the Kerberos realm of the system

* ipa_basedn, the base DN of the LDAP directory

* ipa_domain, the domain configured in IPA

* ipa_server, the IPA server

* ipa_xmlrpc_uri, the XMLRPC URI for IPA requests 

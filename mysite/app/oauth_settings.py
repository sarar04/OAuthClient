import json

#this is based on the oauth2_session.py, more details can get in the file

class settings(object):
	def __init__(self, client_id=None, client=None, scope=None, redirect_uri=None, token=None, state=None, auth_url=None, token_url=None, body=None, 
		auth=None, client_secret=None, method=None, headers=None,timeout=None, verify=None, getinfo_url=None, displayInfo=None):
		""" step 1 : params to Construct a new OAuth 2 client session.
		
		:param client_id: Client id obtained during registration								necessary					
        :param client: :class:`oauthlib.oauth2.Client` to be used. Default is
                       WebApplicationClient which is useful for any
                       hosted application but not mobile or desktop.
        :param scope: List of scopes you wish to request access to 							 	google needed				
        :param redirect_uri: Redirect URI you registered as callback 							sina needed
        :param token: Token dictionary, must include access_token
                      and token_type.
        :param state: State string used to prevent CSRF. This will be given
                      when creating the authorization url and must be supplied
                      when parsing the authorization response.
                      Can be either a string or a no argument callable.

        step 2: params to Form an authorization URL.
        :param auth_url: Authorization endpoint url, must be HTTPS. 							 necessary			

        step 3: params for Generic method for fetching an access token from the token endpoint.
		:param token_url: Token endpoint URL, must use HTTPS. 						 			 necessary
        :param body: Optional application/x-www-form-urlencoded body to add the
                     include in the token request. Prefer kwargs over body.
        :param auth: An auth tuple or method as accepted by requests.
        :param client_id: Username used by LegacyApplicationClients. 							 same as step 1
        :param client_secret: Password used by LegacyApplicationClients. 						 necessary
        :param method: The HTTP method used to make the request. Defaults
                       to POST, but may also be GET. Other methods should
                       be added as needed.
        :param headers: Dict to default request headers with.
        :param timeout: Timeout of the request in seconds.
        :param verify: Verify SSL certificate.

        step 4:  params for display infomation --- based on the authorization web
        :param getinfo_url: url for get infomation												necessary
        :param displayInfo: the process infomation you want to get 								necessary
        """
		self.client_id=client_id
		self.client=client
		self.scope=scope
		self.redirect_uri=redirect_uri
		self.token=token
		self.state=state
		self.auth_url=auth_url
		self.token_url=token_url
		self.body=body
		self.auth=auth
		self.client_secret=client_secret
		self.method=method
		self.headers=headers
		self.timeout=timeout
		self.verify=verify
		self.getinfo_url=getinfo_url
		self.displayInfo=displayInfo

def form_params(oauth_web):
		if oauth_web == 'github':
			obj=github
		elif oauth_web == 'google':
			obj=google
		elif oauth_web == 'sina':
			obj=sina
		else:
			pass

		d = {
			'client_id':		obj.client_id,
			'client':			obj.client,
			'scope':			obj.scope,
			'redirect_uri':		obj.redirect_uri,
			'token':			obj.token,
			'state':			obj.state,
			'auth_url':			obj.auth_url,
			'token_url':		obj.token_url,
			'body':				obj.body,
			'auth':				obj.auth,
			'client_secret':	obj.client_secret,
			'method':			obj.method,
			'headers':			obj.headers,
			'timeout':			obj.timeout,
			'verify':			obj.verify,
			'getinfo_url':		obj.getinfo_url,
			'displayInfo':		obj.displayInfo
		}

		return d



google = settings()
	
	



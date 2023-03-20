import validators

from urllib.parse import urlparse

from secsy.definitions import *
from secsy.tasks._categories import HTTPCommand


class katana(HTTPCommand):
	"""Next-generation crawling and spidering framework."""
	cmd = 'katana -silent -jc -js-crawl -known-files all'
	file_flag = '-list'
	input_flag = '-u'
	json_flag = '-json'
	opt_key_map = {
		HEADER: 'headers',
		DELAY: 'delay',
		DEPTH: 'depth',
		FOLLOW_REDIRECT: OPT_NOT_SUPPORTED,
		MATCH_CODES: OPT_NOT_SUPPORTED,
		METHOD: OPT_NOT_SUPPORTED,
		PROXY: 'proxy',
		RATE_LIMIT: 'rate-limit',
		RETRIES: 'retry',
		THREADS: 'concurrency',
		TIMEOUT: 'timeout',
		USER_AGENT: OPT_NOT_SUPPORTED
	}
	opt_value_map = {
		DELAY: lambda x: int(x) if isinstance(x, float) else x
	}
	output_map = {
		URL: lambda x: x['request']['endpoint'],
		HOST: lambda x: urlparse(x['request']['endpoint']).netloc,
		TIME: 'timestamp',
		METHOD: lambda x: x['request']['method'],
		STATUS_CODE: lambda x: x['response'].get('status_code'),
		CONTENT_TYPE: lambda x: x['response'].get('content_type', ';').split(';')[0]
	}
	install_cmd = 'go install -v github.com/projectdiscovery/katana/cmd/katana@latest'
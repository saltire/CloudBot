# Plugin by Lukeroge

from util import hook
from util import http

api_url = 'http://api.wolframalpha.com/v2/query?format=plaintext'


@hook.command("time")
def time_command(inp, bot=None):
    ".time <area> -- Gets the time in <area>"

    query = "current time in %s" % inp
	
    api_key = bot.config.get("api_keys", {}).get("wolframalpha", None)
    if not api_key:
        return "error: no wolfram alpha api key set"

    request = http.get_xml(api_url, input=query, appid=api_key)
    time = " ".join(request.xpath("//pod[@title='Result']/subpod/plain" \
                    "text/text()"))
    time = time.replace("  |  ", ", ")
    place = " ".join(request.xpath("//pod[@title='Input interpretation']/" \
                     "subpod/plaintext/text()"))[16:].title()

    if time:
	    # if wolfram alpha had to guess a place, then show the place it chose
        #if request.xpath("//assumptions"):
        #    return "%s - \x02%s\x02" % (time, place)
        #else:
        #    return time
		return "%s - \x02%s\x02" % (time, place)
    else:
        return "Could not get the time for '%s'" % inp
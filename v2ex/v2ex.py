# created by Zihan Qi
# 2017/10/08
#!/usr/bin/python
import sys
from workflow import Workflow, web

ICON_DEFAULT = 'icon.png'

def today():
    url = 'https://www.v2ex.com/api/topics/hot.json'
    r = web.get(url)
    # throw an error if request failed
    r.raise_for_status()
    data = r.json()
    return data

def main(wf):
    news = wf.cached_data('today', today, max_age=60)
    for n in news:
        wf.add_item(title=n['title'],
                    subtitle=n['content'],
                    arg=n['url'],
                    valid=True,
                    icon=ICON_DEFAULT)
    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    logger = wf.logger
    sys.exit(wf.run(main))

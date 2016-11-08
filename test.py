from ghost import Ghost, GhostTimeoutError
import logging
import time

logging.basicConfig(level=logging.DEBUG, format='%(levelname)1.1s %(name)s: %(message)s')

ghost = Ghost()

url = 'https://www.baidu.com/'
with ghost.session() as session:
    page, _ = session.open(url)
    text = page.text.encode('UTF-8')
    print text
    session.show()
    session.evaluate("document.getElementById('kw').value='ab';document.getElementById('su').click();",
                     expect_loading=True)

    time.sleep(10)

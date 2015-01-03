# Posts scraper

Basic scraper for custom forums (currently dou.ua only).

## Installation

1. Create virtualenv: `virtualenv . --no-site-packages`
2. Activate it: `source bin/activate`
3. Install requirements: `pip install -r requirements.txt`
4. Create db, add details to settings.py and alembic.ini
5. Run migrations `alembic upgrade head`

## Usage

To grab data: `scrapy crawl dou` or any new spider you will create

## Q&A
**Q:** What is the reason for yet another scrapy based simple project?<br/>
**A:** I have to do some data mining with real world data


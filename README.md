# slack-feedback-bot

**Design**:

cron task calls periodic.py

config: {
  
}


itemizer = PRItemizer() 
scraper = SlackScraper(channel_name, itemizer)





SlackScrapper(channel string, itemizer Itemizer)
- parse() Items

Itemizer interface:
- parse_message(msg)
- 


import insta_scraper as instagram
import database_manager as dbm
import time

table = dbm.getTable("test01", "Enterprise")
table_size = len(table)
for index, row in enumerate(table, start=1):
    enterprise_name = row[0]
    account_id =row[1]
    instagram.getAccountpage(account_id)
    time.sleep(3)
    num_of_post = instagram.getAccountData(instagram.InfoType.POST_COUNT)
    dbm.updateNumOfPosts(enterprise_name, num_of_post)
    print(f'[ {index} / {table_size} ] 완료')

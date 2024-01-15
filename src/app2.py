import insta_scraper as instagram
import database_manager as dbm
import time

table = dbm.getTable("test01", "Enterprise_sorted")
table_size = len(table)
new_table = dbm.getTable("test01", "Post_ver_5")

for index, row in enumerate(table[106:], start=107):
    enterprise_name = row[0]
    account_id = row[1]
    num_of_post = int(row[2])
    try:
        instagram.getAccountpage(account_id)
    except Exception as e:
        instagram.refreshPage()
    time.sleep(3)

    instagram.clickFirstPost()

    for number in range(num_of_post):
        post = {
            "enterprise_name": enterprise_name,
            "num_of_likes": instagram.getNumOfLikes(),
            "published_date": instagram.getPostedDate(),
            "url": instagram.getPostURL(),
        }

        dbm.addRow_Post(post)
        time.sleep(0.5)
        try:
            instagram.clickButton(instagram.ButtonDirection.RIGHT)
        except Exception as e:
            print(f"( {index} / {table_size} ) {enterprise_name} 수집완료")
            break

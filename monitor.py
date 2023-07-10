# To monitor the sites make sure that them are alived

import configparser, requests, os

# root path
root_path = "/home/tommygood/sitesAlived"

# config
config = configparser.ConfigParser()
config.read(root_path + '/config.ini')

# bot_token
bot_token = config["telegram_env"]["bot_token"]

# all chat id of admins need to be notified with telegram bot
all_admin = eval(config["telegram_env"]["chat_id"])

# all the sites are need to be monitored
all_sites = eval(config["target"]["sites"])

def main() :
    # monitor the status of the sites
    monitorSites()

# monitor the status of the sites
def monitorSites() :
    for site in all_sites :    
        # exception will orcur when site is not existed
        try :
            # send request to target site
            res = str(requests.get(site)) 
            # if the response of target site is not the nomral code : 200
            if not res == "<Response [200]>" :
                # send the error message
                msg = f"Site Error : {res} \n {site}" 
                sendMsg(msg)
        # site is not existed
        except Exception as e :
            sendMsg(f"Site Error : {site}\n" + str(e))

# send the monitor result to all admin
def sendMsg(content) :
    # send with bot
    for admin in all_admin :
        send_msg_url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={admin}&text={content}"
        res = requests.get(send_msg_url) # this sends the message
        #print(res)

main()
    

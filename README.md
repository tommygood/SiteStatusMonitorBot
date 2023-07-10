# SiteStatusMonitorBot

## Intro

- auto monitor whether the status of target sites is normal and send the alert message with telegram bot

## Configuration

- `config.ini`
  
  ```
  [telegram_env]

  bot_token = {telegram_bot_token}
  
  chat_id = ["admin_chat_id", "admin1_chat_id"]
  
  [target]
  
  sites = ["https://www.target1.com", "https://www.target2.com"]
  ```

- `monitor.py`

  ```
  # root path
  root_path = "{path_to_file}"
  ```

## Usage

- `crontab -e` : set to monitor each 10 min

  ```
  */10 * * * * python3 /path/to/sitesAlived/monitor.py
  ```

## Demo

![image](https://github.com/tommygood/SiteStatusMonitorBot/assets/96759292/ae1ffa1f-6957-4a7a-92dc-a70e55367ff8)

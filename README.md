# HttpNotifications
Small python script which sends out a pushbullet notification when a website has updated their content based on regex rules.

## Usage
1. To enable Pushbullet, add a file named api_key with your PushBullet API key to the same folder as the script. The key can be found at https://www.pushbullet.com/#settings.
2. python compare.py url regex t_index l_index [force]

#### Mandatory Parameters
URL - (http://github.com): The URL to the website to access.

Regex - (/test/g): The string with the rule which pickes out a title and a link to the contents. (TO ADD: If no link is found, use the URL)

Title Index - (1-2): The regex group index of the title. If found BEFORE the link [1]

Link Index - (1-2): The regex group index of the link.If found AFTER the title [2]

#### Optional Parameters
Force - (force): Should a message be sent even if nothing has been updated. Good for debugging.

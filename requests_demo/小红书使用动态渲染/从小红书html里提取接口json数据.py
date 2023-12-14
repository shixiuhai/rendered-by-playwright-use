import re

html_content = "<html><head><meta name=\"color-scheme\" content=\"light dark\"></head><body><pre style=\"word-wrap: break-word; white-space: pre-wrap;\">{\"data\":{\"comments\":[],\"has_more\":false,\"time\":1702554945904,\"user_id\":\"657aec3100000000200350eb\"},\"code\":0,\"success\":true,\"msg\":\"成功\"}\n</pre></body></html>"

# 使用正则表达式提取 JSON 数据
json_match = re.search(r'<pre.*?>(.*?)</pre>', html_content, re.DOTALL)

if json_match:
    json_data = json_match.group(1)
    print(json_data)
else:
    print("未找到匹配的 JSON 数据")
